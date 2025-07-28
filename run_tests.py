import subprocess
import sys
import os

def run_tests():
    """
    Run pytest with coverage report, fixing Python path.
    """
    print("Running tests with coverage report...\n")
    # Add current directory to PYTHONPATH
    os.environ["PYTHONPATH"] = os.getcwd()
    command = ["pytest", "--cov=services", "--cov-report=term-missing", "tests/"]
    result = subprocess.run(command)
    sys.exit(result.returncode)

if __name__ == "__main__":
    run_tests()
