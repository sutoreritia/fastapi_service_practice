import re


ORDERS = {
    "K1001": {
        "delivery_status": "配送中",
        "estimated_arrival": "2026-06-23 15:30",
    },
    "K1002": {
        "delivery_status": "備貨中",
        "estimated_arrival": "2026-06-24 10:00",
    },
    "K1003": {
        "delivery_status": "已完成",
        "estimated_arrival": "已送達",
    },
}


def extract_order_id(text: str) -> str | None:
    """從文字中擷取訂單編號，例如 K1001。"""
    match = re.search(r"\b[A-Z]\d{4}\b", text)

    if match is None:
        return None

    return match.group(0)


def get_order_status(order_id: str):
    """查詢訂單配送狀態。"""
    order = ORDERS.get(order_id)

    if not order:
        return {
            "success": False,
            "order_id": order_id,
            "message": f"查無訂單 {order_id}",
        }

    return {
        "success": True,
        "order_id": order_id,
        "delivery_status": order["delivery_status"],
        "estimated_arrival": order["estimated_arrival"],
    }