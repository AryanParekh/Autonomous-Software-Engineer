import docker
import os

def run_tests_in_docker(workspace_path: str):
    """
    Runs pytest inside a Docker container using the code in workspace_path.
    """
    client = docker.from_env()
    
    # Absolute path is required for Docker volumes
    abs_path = os.path.abspath(workspace_path)
    
    print(f"   🐳 Spinning up Docker container...")
    
    try:
        # Run a temporary container
        # We mount the local 'workspace' folder to '/app' inside the container
        container = client.containers.run(
            image="python:3.9-slim",
            command="/bin/bash -c 'pip install pytest && pytest /app/test_solution.py'",
            volumes={abs_path: {'bind': '/app', 'mode': 'rw'}},
            working_dir="/app",
            detach=True,
            remove=True  # Automatically delete container after run
        )
        
        # Wait for it to finish and get logs
        # Note: simpler approach for short scripts
        result = container.wait()
        logs = container.logs().decode("utf-8")
        
        exit_code = result.get('StatusCode', 1)
        
        return exit_code, logs

    except Exception as e:
        return 1, f"Docker Error: {str(e)}"