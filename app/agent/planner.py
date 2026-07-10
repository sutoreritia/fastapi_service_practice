from app.tools.order_tools import extract_order_id


def plan_task(task):
    # 1. 全部轉小寫，方便比對
    text = task.lower()

    # 2. 試著抓看看有沒有單號（不一定有）
    order_id = extract_order_id(task)

    # 3. 保安系統啟動！檢查高風險關鍵字
    if "退款" in task or "取消" in task or "刪除" in task:
        return {
            "task_type": "manual_review",
            "selected_tool": "none",
            "parameters": {},
            "confidence": 0.9,
            "reason": "任務涉及高風險操作，需要人工審核。",
            "need_human_review": True,
        }

    # 4. 如果有抓到單號，那就是查訂單！
    if order_id:
        return {
            "task_type": "order_status",
            "selected_tool": "get_order_status",
            "parameters": {"order_id": order_id},
            "confidence": 0.95,
            "reason": "包含單號，查詢訂單。",
            "need_human_review": False,
        }

    # 5. 如果有提到庫存缺貨
    if "低庫存" in text or "缺貨" in text:
        return {
            "task_type": "inventory_check",
            "selected_tool": "get_low_stock_items",
            "parameters": {},
            "confidence": 0.9,
            "reason": "與庫存相關。",
            "need_human_review": False,
        }

    # 6. 如果有提到營運摘要
    if "營運摘要" in text or "今日摘要" in text:
        return {
            "task_type": "ops_summary",
            "selected_tool": "generate_ops_summary",
            "parameters": {"date": "2026-06-23"},
            "confidence": 0.85,
            "reason": "要求產生營運摘要。",
            "need_human_review": False,
        }

    # 7. 如果都聽不懂
    return {
        "task_type": "unknown",
        "selected_tool": "none",
        "parameters": {},
        "confidence": 0.3,
        "reason": "無法判斷。",
        "need_human_review": True,
    }