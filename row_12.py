from flask import Flask, request, render_template_string

app = Flask(__name__)

# Sample template
TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ name }}</title>
</head>
<body>
    <h1>Hello, {{ name }}!</h1>
</body>
</html>
"""

def render_response_from_env(env):
    # Get the 'name' parameter from the query string or form data
    name = request.args.get('name')  # You can change this to request.form['name'] if using a form
    if not name:
        return "Name parameter is required.", 400

    # Get the template from the environment (in this case, just use our hardcoded template)
    template = TEMPLATE

    # Render the template with the provided name
    rendered_template = render_template_string(template, name=name)

    # Return a response with the rendered template
    return rendered_template

@app.route('/')
def home():
    env = {}  # Typically, this would be your environment setup (e.g., database connections, configurations)
    response = render_response_from_env(env)
    return response

if __name__ == '__main__':
    app.run(debug=True)
bash
python app.py