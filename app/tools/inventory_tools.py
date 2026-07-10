from app.data.mock_data import INVENTORY

# 功能 1 : 列出所有庫存
def list_inventory():
    return {"success": True, "items": INVENTORY}

# 功能 2 : 找出低庫存品項
def get_low_stock_items():
    items = [
        item for itwm in INVENTORY
        if item["stock"] < item["safe_stock"]
    ]
    return {"success": True, "count": len(items), "items": items}