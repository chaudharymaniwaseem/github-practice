
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>My GitHub Practice Project</title>
        </head>
        <body>
            <h1>Welcome to My Docker Project!</h1>
            <p>I am learning Python, Docker, Git, and GitHub.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
