from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "TARGETING " + request.args.get("text")

if __name__ == "__main__":
    user_agent = "Urban-slack/1.0 (https://github.com/t3h2mas/urban-slack; t.homas.noee@gmail.com)"

    app.run()
