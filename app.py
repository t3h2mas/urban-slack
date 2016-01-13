from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == "__main__":
    user_agent = "Urban-slack/1.0 (https://github.com/t3h2mas/urban-slack; t.homas.noee@gmail.com)"

    app.run()
