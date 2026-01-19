from typing import Literal
from langgraph.graph import StateGraph, END
from src.core.state import AgentState
from src.agents.developer import developer_node
from src.agents.tester import tester_node
from src.runtime.executor import executor_node

def should_continue(state: AgentState) -> Literal["developer", END]:
    if state['iterations'] > 3:
        return END
    if state['error'] != "None":
        return "developer"
    return END

def create_graph():
    workflow = StateGraph(AgentState)

    # Nodes
    workflow.add_node("developer", developer_node)
    workflow.add_node("tester", tester_node)
    workflow.add_node("executor", executor_node)

    # Edges
    workflow.set_entry_point("developer")
    workflow.add_edge("developer", "tester")
    workflow.add_edge("tester", "executor")
    
    # Conditional Loop
    workflow.add_conditional_edges(
        "executor",
        should_continue,
        {
            "developer": "developer",
            END: END
        }
    )

    return workflow.compile()