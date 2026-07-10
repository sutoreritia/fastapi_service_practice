from pydantic import BaseModel, Field


# 1. 使用者傳來的任務
class AgentTaskRequest(BaseModel):
    task: str = Field(min_length=1, max_length=500)


# 2. Planner 思考出的「行動計畫」
class AgentPlan(BaseModel):
    task_type: str             # 這是哪種任務？
    selected_tool: str         # 決定用哪個工具？
    parameters: dict           # 要傳給工具什麼參數？
    confidence: float          # 大腦有多確定？(0.0~1.0)
    reason: str                # 為什麼做這個決定？
    need_human_review: bool    # 是否有危險，需要人類審核？


# 3. 系統最後回傳給使用者的總結
class AgentRunResponse(BaseModel):
    task: str                  # 原始任務
    plan: AgentPlan            # 上面的計畫
    tool_result: dict          # 工具執行的結果
    final_answer: str          # 白話文解答
    next_action: str           # 下一步建議
    need_human_review: bool    # 總結是否需人工