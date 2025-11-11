from flask import Flask, request, redirect
import re

app = Flask(__name__)

# Define the regex pattern
regex = r"https?://.*\.example\.com.*"  # This will match URLs containing example.com

@app.route('/redirect')
def redirect_to_target():
    target = request.args.get('target')

    if target and re.match(regex, target):
        return redirect(target)
    else:
        return redirect('/')  # Redirect to the root URL if the regex does not match

if __name__ == '__main__':
    app.run(debug=True)
bash
pip install flask