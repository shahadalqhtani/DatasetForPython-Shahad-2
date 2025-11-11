from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

# URL to ping is passed as a query parameter 'url'
@app.route('/<url>/ping')
def ping(url):
    # Check if the url is provided in the query parameters
    if not url:
        return "URL not provided", 400

    try:
        # Run the ping command using subprocess
        result = subprocess.run(['ping', '-c', '1', url], capture_output=True, text=True)

        # Check if the ping command was successful (return code is 0)
        if result.returncode == 0:
            pong = "URL is alive"
        else:
            pong = f"Ping to URL failed with error: {result.stderr}"
    except Exception as e:
        # Handle any exceptions that might occur during the ping command execution
        pong = str(e)

    return pong, 200 if result.returncode == 0 else 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')