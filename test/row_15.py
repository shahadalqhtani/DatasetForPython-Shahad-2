import sys
import subprocess

def execute_command(command):
    """Execute a command and return its output."""
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing the command: {e.stderr.decode('utf-8')}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <username>")
        sys.exit(1)

    username = sys.argv[1]
    command = f"cat /etc/passwd | grep {username}"
    output = execute_command(command)

    # Use awk to format the output more clearly if needed, or simply print lines that match the username
    for line in output.splitlines():
        if username in line:
            print(line)

if __name__ == "__main__":
    main()
bash
python get_userinfo.py <username>