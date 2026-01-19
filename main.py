from src.core.logger import initialize_logs, Colors
from src.workflow import create_graph

if __name__ == "__main__":
    # 1. Setup
    initialize_logs()
    app = create_graph()
    
    # 2. Define Mission
    requirement = """
        Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

        Function Signature:
        def trap(height: List[int]) -> int:

        Example 1:
        Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
        Output: 6
        Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

        Example 2:
        Input: height = [4,2,0,3,2,5]
        Output: 9

        Constraints:
        - n == height.length
        - 1 <= n <= 2 * 10^4
        - 0 <= height[i] <= 10^5
    """
    
    initial_state = {
        "requirement": requirement,
        "code": "",
        "tests": "",
        "error": "None",
        "iterations": 0
    }

    print(f"{Colors.HEADER}Starting Autonomous Agent...{Colors.ENDC}")
    print(f"{Colors.WARNING}🎯 REQUIREMENT: LeetCode Hard - Trapping Rain Water (Unsafe Mode){Colors.ENDC}\n")
    app.invoke(initial_state)