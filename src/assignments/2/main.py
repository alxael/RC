from flask import Flask, jsonify
from flask import request

app = Flask(__name__)


@app.route('/')
def main():
    return jsonify({
        "mergem la vot?": "da"
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
