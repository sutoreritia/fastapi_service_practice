from app.agent.planner import plan_task


# 測試 1：正常查單任務
def test_plan_order_task():
    plan = plan_task("請幫我查 K1001 配送狀態")
    assert plan["task_type"] == "order_status"
    assert plan["selected_tool"] == "get_order_status"
    assert plan["parameters"]["order_id"] == "K1001"


# 測試 2：高風險保安測試！
def test_plan_high_risk_task():
    plan = plan_task("我要取消 K1001 並退款！")
    assert plan["task_type"] == "manual_review"
    assert plan["need_human_review"] is True