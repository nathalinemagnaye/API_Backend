from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '').strip().lower()

    if user_message == 'hi':
        response = "hello"
    else:
        response = "i don't understand"

    return jsonify({'reply': response})

if __name__ == '__main__':
    app.run(debug=True)
