# FastAPI Service Practice — HTTP Endpoints & Rule-Based Operations Assistant

[English](#english) · [繁體中文](#繁體中文)

## English

A **Python backend learning repository** with two separate entry points:

1. A small **FastAPI web service** exposing health and version endpoints.
2. A **rule-based command-line operations assistant** for a central-kitchen scenario, with task planning, tool dispatch, and JSON logs.

The assistant currently uses **keyword rules and simulated data, not an LLM**. The HTTP endpoints in `main.py` do **not** expose the assistant as an API yet.

## Implemented features

- `GET /health` → `{"status": "ok", "service": "fastapi_service_practice"}`
- `GET /version` → `{"version": "1.0.0", "stage": "learning"}`
- CLI assistant classifies requests involving order status, low inventory, and operations summaries.
- A tool registry routes recognized tasks to functions using sample data.
- High-risk or unclear actions are directed to human review instead of being executed.
- The assistant logs its plan, tool results, and response in a local JSON file.

## Architecture

```text
HTTP client ---> main.py (FastAPI) ---> /health, /version

CLI user -----> cli.py ---> planner ---> executor ---> tool registry
                                   |                |
                              human review     mock order/inventory/summary tools
                                   \                /
                                      agent_service ---> JSON log
```

## Requirements and setup

Python **3.10+**. Use a virtual environment, then install the project dependencies defined in `pyproject.toml`:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e .
```

### Run the web service

```powershell
python -m uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000/health`, `http://127.0.0.1:8000/version`, or interactive API documentation at `http://127.0.0.1:8000/docs`.

### Run the CLI assistant

```powershell
python cli.py
```

Example prompt: `請幫我查 K1001 配送狀態`. Sample order identifiers and dates are **fixtures, not real-time enterprise information**.

### Tests

```powershell
python -m pip install pytest
python -m pytest -q
```

## Important files

- `main.py` — web endpoints
- `cli.py` — interactive terminal UI
- `app/agent/planner.py` — rule-based intent detection and human-review decisions
- `app/agent/executor.py` — tool invocation
- `app/agent/agent_service.py` — orchestration and response assembly
- `app/tools/` — sample operations tools
- `app/agent/memory.py` — local JSON logging
- `tests/` — test cases

## Limitations / next steps

This is a learning prototype, not a deployed agent or LLM-powered assistant. It uses fixed examples, and some sample dates are hard-coded. Future work: expose assistant operations through documented HTTP endpoints, validate request schemas, improve error handling and tests, and move configuration/fixtures into safer production-ready components.

---

## 繁體中文

本專案為 **Python 後端學習作品**，包含兩個獨立入口：

1. **FastAPI Web 服務：** 提供健康檢查與版本資訊的 HTTP API。
2. **中央廚房營運助理（CLI）：** 以規則判斷任務類型，再分派到訂單、庫存或營運摘要工具，並記錄執行結果。

目前助理採用**關鍵字規則與模擬資料，不是 LLM 驅動的 AI Agent**；`main.py` 的 HTTP API 目前也尚未提供助理功能的呼叫端點。

## 已實作功能

- `GET /health`：服務健康檢查，回傳 JSON。
- `GET /version`：服務版本資訊，回傳 JSON。
- 命令列助理：辨識訂單查詢、缺貨／低庫存與營運摘要任務。
- 工具註冊表：將任務分派給對應函式及示範資料。
- 高風險或無法判讀任務：標示需人工處理，不自動執行。
- 使用本機 JSON 檔案記錄規劃、工具結果及回覆。

## 程式架構

```text
HTTP 用戶端 ---> main.py (FastAPI) ---> /health, /version

終端機使用者 ---> cli.py ---> planner ---> executor ---> 工具註冊表
                                       |                 |
                                    人工覆核        模擬訂單／庫存／報表工具
                                         \             /
                                           agent_service ---> JSON 紀錄
```

## 安裝及執行

需求：Python **3.10 以上**。

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e .
```

啟動 HTTP API：

```powershell
python -m uvicorn main:app --reload
```

可瀏覽 `http://127.0.0.1:8000/health`、`http://127.0.0.1:8000/version`，或透過 `http://127.0.0.1:8000/docs` 查看 API 文件。

啟動命令列助理：

```powershell
python cli.py
```

測試輸入：`請幫我查 K1001 配送狀態`。程式中的訂單及日期是**示範資料，不代表真實營運狀態**。

執行測試：

```powershell
python -m pip install pytest
python -m pytest -q
```

## 主要檔案

- `main.py`：HTTP API
- `cli.py`：終端機互動
- `app/agent/planner.py`：規則式任務分類與人工覆核判斷
- `app/agent/executor.py`：執行工具
- `app/agent/agent_service.py`：整合執行結果與回覆
- `app/tools/`：模擬營運工具
- `app/agent/memory.py`：本機 JSON 紀錄
- `tests/`：測試程式

## 限制與下一步

這是學習原型，尚非正式部署的 Agent 或大型語言模型應用。任務判斷依固定規則，部分日期為寫死的範例。後續可以新增真正的任務 API、請求資料驗證、例外處理、更多測試，以及更安全的環境設定。
