from app.tools.inventory_tools import get_low_stock_items

def generate_ops_summary(date):
    low_stock = get_low_stock_items()
    risks = []
    action = []

    if low_stock["count"] > 0:
        names = [item["name"] for item in low_stock["item"]]
        risks.append(f"低庫存品項 : {', '.join(names)}")
        action.append("請採購或中央廚房優先確認地庫存品項補貨。")

    actions.append("請採購或中央廚房配送中與備貨中訂單。")
    return {"success": True, "date": date, "summary": f"(date) 營運摘要", "risks": risks, "suggested_actions": actions}