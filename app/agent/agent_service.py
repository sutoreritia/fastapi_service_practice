from app.agent.executor import execute_plan
from app.agent.memory import append_log
from app.agent.planner import plan_task


def build_final_answer(plan, tool_result):
    if plan["need_human_review"]:
        return "此任務涉及高風險或無法判斷的內容，建議轉交人工處理。"

    if not tool_result.get("success"):
        return f"工具執行失敗：{tool_result.get('message')}"

    if plan["task_type"] == "order_status":
        order_id = tool_result.get("order_id", "未知訂單")
        delivery_status = tool_result.get("delivery_status", "未知狀態")
        estimated_arrival = tool_result.get("estimated_arrival", "未知時間")

        return f"訂單 {order_id} 狀態為 {delivery_status}，預估 {estimated_arrival} 到達。"

    return "任務已完成。"

def build_next_action(plan, tool_result):
    # 如果是高風險，建議永遠是「交給人類」
    if plan["need_human_review"]:
        return "請交由營運主管或人工客服確認。"

    # 如果是查庫存，而且真的有缺貨
    if plan["task_type"] == "inventory_check" and tool_result.get("count", 0) > 0:
        return "請中央廚房確認採購與補貨排程。"

    # 如果是查訂單
    if plan["task_type"] == "order_status":
        return "若配送延誤，請聯繫配送窗口。"

    # 其他狀況的預設建議
    return "請依結果進行後續追蹤。"

# 記得在檔案最上方補上這兩行：
# from app.agent.planner import plan_task
# from app.agent.executor import execute_plan


def run_agent(task):
    # 1. 呼叫大腦思考計畫
    plan = plan_task(task)

    # 2. 呼叫手腳去執行
    tool_result = execute_plan(plan)

    # 3. 翻譯結果與建議
    final_answer = build_final_answer(plan, tool_result)
    next_action = build_next_action(plan, tool_result)

    # 4. 組裝成最終回應
    response = {
        "task": task,
        "plan": plan,
        "tool_result": tool_result,
        "final_answer": final_answer,
        "next_action": next_action,
        "need_human_review": plan["need_human_review"],
    }

    # 待後實作 Memory 後，這裡會加入 append_log
    append_log(response)
    return response