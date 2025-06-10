from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ping')
def ping():
    return "pong"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("📨 웹훅 수신됨:")
    print(data)
    return jsonify({"status": "received"}), 200

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)