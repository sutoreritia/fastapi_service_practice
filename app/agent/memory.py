import json
from pathlib import Path
from app.config import AGENT_LOG_FILE


LOG_PATH = Path(AGENT_LOG_FILE)


def load_logs():
    if not LOG_PATH.exists():
        return []

    # 讀取檔案內容並轉成 JSON 清單
    content = LOG_PATH.read_text(encoding="utf-8")
    if not content.strip():
        return []

    return json.loads(content)


def append_log(record):
    # 1. 拿出現有的記錄
    logs = load_logs()

    # 2. 把新的記錄塞進去
    logs.append(record)

    # 3. 寫回檔案裡！
    LOG_PATH.write_text(
        json.dumps(logs, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )