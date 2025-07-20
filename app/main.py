from flask import Flask, url_for
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    name = os.environ.get("NAME", "Vaibhav")
    # Return a full HTML document with a link to the favicon
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Python-WebApp</title>
        <link rel="shortcut icon" href="{ url_for('static', filename='favicon.ico') }">
    </head>
    <body style="display: flex; justify-content: center; align-items: center; height: 100vh; font-family: sans-serif; margin: 0;">
        <h1 style="color: tomato; text-align: center;">Hello 🙋‍♂️, {name} from Docker!</h1>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)