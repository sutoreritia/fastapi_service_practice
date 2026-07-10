from app.tools.tool_registry import get_tool


def execute_plan(plan):
    # 1. 如果大腦沒有用工具（高風險或聽不懂），就直接回傳沒做事
    if plan["selected_tool"] == "none":
        return {"success": False, "message": "未選擇工具，需人工處理。"}

    # 2. 去註冊表拿工具！
    tool = get_tool(plan["selected_tool"])
    if not tool:
        return {"success": False, "message": "找不到工具！"}

    # 3. 把真正的 function 和 parameters 拿出來
    function = tool["function"]
    parameters = plan["parameters"]
    
    try:
        return function(**parameters)
    except TypeError as exc:
        return {"success": False, "message": f"工具參數錯誤：{exc}"}