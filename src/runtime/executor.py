from src.core.state import AgentState
from src.core.logger import Colors, log_to_markdown
from src.runtime.sandbox import run_tests_in_docker # Your existing docker function

def executor_node(state: AgentState):
    print(f"\n{Colors.BLUE}--- 🐳 Executor is running tests ---{Colors.ENDC}")
    
    exit_code, logs = run_tests_in_docker("./workspace")
    
    status = "✅ PASSED" if exit_code == 0 else "❌ FAILED"
    log_to_markdown("Execution Results", f"**Status:** {status}\n```text\n{logs}\n```")
    
    if exit_code == 0:
        print(f"{Colors.GREEN}   ✅ Success!{Colors.ENDC}")
        return {"error": "None"}
    else:
        print(f"{Colors.FAIL}   ❌ Failure!{Colors.ENDC}")
        return {"error": logs}