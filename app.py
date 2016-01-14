from flask import Flask, request
import urban
app = Flask(__name__)

@app.route('/')
def hello_world():
    word = request.args.get("text")
    results = urban.lookup(word)
    return "\n".join(results)

if __name__ == "__main__":
    app.run()
