from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_run_agent_order_task():
    response = client.post(
        "/agent/run",
        json={"task": "請幫我查 K1001 配送狀態"},
    )

    assert response.status_code == 200

    data = response.json()

    assert data["task"] == "請幫我查 K1001 配送狀態"
    assert data["plan"]["task_type"] == "order_status"
    assert data["plan"]["selected_tool"] == "get_order_status"
    assert data["tool_result"]["success"] is True
    assert data["tool_result"]["order_id"] == "K1001"
    assert "配送中" in data["final_answer"]