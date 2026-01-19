import os
import time

# Define the workspace directory relative to the project root
# (Since we run main.py from root, 'workspace' is created there)
WORKSPACE_DIR = "workspace"
LOG_FILE = os.path.join(WORKSPACE_DIR, "mission_report.md")

class Colors:
    """ANSI Escape codes for terminal colors."""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def initialize_logs():
    """
    Creates the workspace directory and wipes the previous mission report.
    This runs once at the start of the program.
    """
    os.makedirs(WORKSPACE_DIR, exist_ok=True)
    
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write(f"# 🚀 Mission Report\n")
        f.write(f"**Target:** Autonomous Coding Agent\n")
        f.write(f"**Date:** {time.ctime()}\n\n")
        f.write("---\n\n")

def log_to_markdown(section_title: str, content: str, emoji: str = "📄"):
    """
    Appends a formatted section to the markdown report.
    
    Args:
        section_title: The H2 header for the section
        content: The body text (can include markdown syntax)
        emoji: An icon to make the header look nice
    """
    os.makedirs(WORKSPACE_DIR, exist_ok=True)
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"## {emoji} {section_title}\n\n")
        f.write(f"{content}\n\n")
        f.write("---\n\n")

def save_to_file(filename: str, content: str):
    """
    Saves generated code (solution.py, test_solution.py) to the workspace.
    
    Args:
        filename: Name of the file (e.g., 'solution.py')
        content: The Python code string
    """
    os.makedirs(WORKSPACE_DIR, exist_ok=True)
    filepath = os.path.join(WORKSPACE_DIR, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    return filepath