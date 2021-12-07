from flask import Flask

# instance of Flask
app = Flask(__name__)

# default route
@app.route("/")
def index():
    return "Welcome! to Index Page"

@app.route("/hello")
def hello_world():
    return "<h1>Hello, World!</h1>"

# /user
@app.route("/user/<username>")
def hello_user(username):
    return f"Welcome!, {username}"


if __name__ == "__main__":
    app.run(host='0.0.0.0')