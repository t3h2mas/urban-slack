from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        word = request.args.get('text', '')
        return "looking up {}".format(word)
    return 'Hello World!'

if __name__ == "__main__":
    user_agent = "Urban-slack/1.0 (https://github.com/t3h2mas/urban-slack; t.homas.noee@gmail.com)"

    app.run(port=80)
