import subprocess
import sys

def execute_command(command):
    """Execute a given command."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <username>")
        sys.exit(1)

    username = sys.argv[1]
    command = f"cat /etc/passwd | grep {username}"
    output = execute_command(command)

    if output:
        print(output)
    else:
        print("User not found.")
sh
python3 script.py <username>
sh
python3 script.py john