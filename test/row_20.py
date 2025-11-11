from flask import Flask, request, jsonify
import subprocess
import sys

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_code():
    code = request.json.get('code')

    if not code:
        return "Code is required", 400

    try:
        # Execute the code in a separate Python process to isolate it from the server environment
        result = subprocess.run([sys.executable, '-c', code], capture_output=True, text=True)

        # Prepare the output including standard error if there was any
        output = {
            'stdout': result.stdout,
            'stderr': result.stderr,
            'returncode': result.returncode
        }

        return jsonify(output), 200
    except Exception as e:
        return f"Error executing the code: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)
bash
curl -X POST http://localhost:5000/execute -H "Content-Type: application/json" -d '{"code": "print('Hello,
World!')", "input": ""}'