from flask import Flask, request, jsonify
import urban
app = Flask(__name__)

def craft_response(results):
    r = {}
    r['response_type'] = "in_channel"
    r['text'] = results[0]
    r['attachments'] = [{'text': results[1]}]
    return r

@app.route('/')
def hello_world():
    word = request.args.get("text")
    results = urban.lookup(word)
    return jsonify(craft_response(results))

if __name__ == "__main__":
    app.run()
