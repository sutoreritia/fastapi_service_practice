from fastapi import APIRouter, HTTPException
from app.agent.agent_service import run_agent
from app.agent.schemas import AgentRunResponse, AgentTaskRequest


router = APIRouter(prefix="/agent", tags=["agent"])


@router.post("/run", response_model=AgentRunResponse)
def run_agent_task(request: AgentTaskRequest):
    
    task = request.task.strip()

    
    if not task:
        raise HTTPException(status_code=400, detail="task 不可為空白")

    
    return run_agent(task)