from langchain_core.messages import SystemMessage, HumanMessage
from src.core.config import get_llm
from src.core.state import AgentState, AgentOutput
from src.core.logger import Colors, log_to_markdown, save_to_file

llm = get_llm()

def developer_node(state: AgentState):
    iter_count = state['iterations'] + 1
    print(f"\n{Colors.BLUE}--- 👨‍💻 Developer is working (Iteration {iter_count}) ---{Colors.ENDC}")

    # SYSTEM PROMPT: The Guardrails
    system_instruction = (
        "You are a Principal Software Engineer. You write robust, production-grade code.\n"
        "STRICT OUTPUT RULES:\n"
        "1. Return ONLY valid Python code (imports + functions).\n"
        "2. DO NOT include 'Example usage' or 'if __name__ == \"__main__\":' blocks.\n"
        "3. This code is a LIBRARY MODULE. Global execution code will break the build.\n"
        "4. Keep thoughts concise."
    )
    
    prompt = f"Requirement: {state['requirement']}"

    # Audit Loop Logic
    if state.get('error') and state['error'] != "None":
        print(f"{Colors.WARNING}   ⚠️ Feedback received: Auditing Failure...{Colors.ENDC}")
        prompt += (
            f"\n\n🚨 PREVIOUS FAILURE:\n{state['error']}\n"
            f"TEST SUITE:\n{state['tests']}\n"
            "INSTRUCTION: Calculate expected values manually. If the Test is wrong, add a '# NOTE:' comment. If Code is wrong, fix it."
        )

    messages = [SystemMessage(content=system_instruction), HumanMessage(content=prompt)]
    
    # Generate
    structured_llm = llm.with_structured_output(AgentOutput)
    response = structured_llm.invoke(messages)
    
    # Side Effects (Saving/Logging)
    save_to_file("solution.py", response.code)
    log_to_markdown(f"Developer Iteration {iter_count}", 
                    f"**Thoughts:** {response.thought_process}\n\n```python\n{response.code}\n```")
    
    return {"code": response.code, "iterations": iter_count, "error": "None"}