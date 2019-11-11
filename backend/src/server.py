from flask import Flask, request, jsonify
from firebase import writePost

app = Flask(__name__)

@app.route('/submit_post', methods=['POST'])
def submit_post():
    print(request.json)
    return jsonify({"status": "success"}), 201

if __name__ == "__main__":
    app.run()