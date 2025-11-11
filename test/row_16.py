from flask import Flask, request, send_file
import os

app = Flask(__name__)

# Define the directory where files are stored (this is for demonstration purposes)
FILE_STORAGE_DIR = "/path/to/store/files"  # Update this path to your desired storage location

@app.route('/', methods=['GET'])
def read_file():
    filename = request.args.get('filename')

    if not filename:
        return "Filename is required", 400

    file_path = os.path.join(FILE_STORAGE_DIR, filename)

    if not os.path.exists(file_path):
        return f"File '{filename}' does not exist", 404

    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        return f"Error reading the file: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)