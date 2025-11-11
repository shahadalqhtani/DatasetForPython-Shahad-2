from flask import Flask, request, redirect, render_template

app = Flask(__name__)

# In-memory storage for messages; replace this with your actual database logic
messages = []

def insert_user_message_in_db(username, message):
    # This function should handle the insertion of the username and message into your database.
    # For now, we'll just append to our in-memory list.
    messages.append({"username": username, "message": message})

@app.route('/', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        username = request.form['username']
        message = request.form['message']
        insert_user_message_in_db(username, message)
        return redirect('/')  # Redirect to the main page after posting a new message
    else:
        # Render the template with the existing messages
        return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Messages</title>
</head>
<body>
    <h1>Messages</h1>
    <ul>
        {% for message in messages %}
            <li>{{ message.username }} says: {{ message.message }}</li>
        {% endfor %}
    </ul>
    <form action="/" method="post">
        Username: <input type="text" name="username"><br>
        Message: <input type="text" name="message"><br>
        <input type="submit" value="Post">
    </form>
</body>
</html>