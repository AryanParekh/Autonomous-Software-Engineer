from typing import TypedDict
from pydantic import BaseModel, Field

class AgentOutput(BaseModel):
    thought_process: str = Field(
        description="Strictly concise reasoning (bullet points, max 50 words)."
    )
    code: str = Field(
        description="The valid Python code or test module. No conversational text."
    )

class AgentState(TypedDict):
    requirement: str
    code: str
    tests: str
    error: str
    iterations: int