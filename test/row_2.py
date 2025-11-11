import subprocess

def list_directory(path):
    # Create a format string for the print function
    format_string = "Listing directory: {}\n"

    # Print the path and pass it as an argument to the format string
    print(format_string.format(path))

    try:
        # Execute the ls command with the given path as an argument
        result = subprocess.run(['ls', '-l', path], capture_output=True, text=True)

        # Print the output of the ls command if it executed successfully
        print(result.stdout)
    except FileNotFoundError:
        # Handle the case where the directory does not exist or the user lacks permissions
        print("The specified path does not exist or you do not have permission to access it.")

# Example usage of the function
list_directory('/path/to/directory')