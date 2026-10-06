from flask import Flask

app = Flask(__name__)

# localhost:8080/
@app.route("/")
def hello_world():
    return "<p>Hello, My name is Malaika, nice to meet you!</p>"