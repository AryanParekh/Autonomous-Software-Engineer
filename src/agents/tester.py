from langchain_core.messages import SystemMessage, HumanMessage
from src.core.config import get_llm
from src.core.state import AgentState, AgentOutput
from src.core.logger import Colors, log_to_markdown, save_to_file

llm = get_llm()

def tester_node(state: AgentState):
    print(f"\n{Colors.BLUE}--- 🕵️‍♂️ QA Team is working ---{Colors.ENDC}")
    
    system_instruction = (
        "You are a Lead QA Engineer. You are paranoid about edge cases.\n"
        "RULES:\n"
        "1. Write a complete 'pytest' script.\n"
        "2. Generate 10+ varied test cases (Happy Path, Edge Cases, Invalid Inputs).\n"
        "3. Respect '# NOTE' comments from the Developer if they dispute your math."
    )
    
    prompt = (
        "Write a pytest script for the following code.\n"
        "CRITICAL RULE: Import the function from 'solution'. \n"
        f"Code:\n{state['code']}"
    )

    if state.get('error') and state['error'] != "None":
        prompt += f"\n\n🚨 PREVIOUS FAILURE:\n{state['error']}\nFix the test suite if needed."

    messages = [SystemMessage(content=system_instruction), HumanMessage(content=prompt)]
    
    structured_llm = llm.with_structured_output(AgentOutput)
    response = structured_llm.invoke(messages)
    
    save_to_file("test_solution.py", response.code)
    log_to_markdown("QA Strategy", f"**Thoughts:** {response.thought_process}\n\n```python\n{response.code}\n```")
    
    return {"tests": response.code}