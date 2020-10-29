from flask import Flask

app = Flask(__name__)


@app.rout('/')
def index():
    return "HELLO"


if __name__ == '__main__':
    app.run(port=80, host='127.0.0.1')
