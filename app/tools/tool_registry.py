from app.tools.inventory_tools import get_low_stock_items, list_inventory
from app.tools.order_tools import get_order_status
from app.tools.summary_tools import generate_ops_summary


TOOL_REGISTRY = {
    "get_order_status": {
        "name": "get_order_status",
        "description": "查詢訂單配送狀態。",
        "function": get_order_status,
        "risk": "low",
    },
    "list_inventory": {
        "name": "list_inventory",
        "description": "查詢目前庫存",
        "function": list_inventory,
        "risk": "low",
    },
    "get_low_stock_items": {
        "name": "get_low_stock_items",
        "description": "查詢缺貨品項",
        "function": get_low_stock_items,
        "risk": "low",
    },
    "generate_ops_summary": {
        "name": "generate_ops_summary",
        "description": "產生營運摘要",
        "function": generate_ops_summary,
        "risk": "medium",
    },
}


def get_tool(tool_name):
    return TOOL_REGISTRY.get(tool_name)


def list_tools():
    return [
        {
            "name": tool["name"],
            "description": tool["description"],
            "risk": tool["risk"],
        }
        for tool in TOOL_REGISTRY.values()
    ]