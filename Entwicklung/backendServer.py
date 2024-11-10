from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    data = {
        'message': 'Hello, world!',
        'status': 'success'
    }
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def receive_data():
    if request.is_json:
        content = request.get_json()
        response = {
            'received_data': content,
            'status': 'data received'
        }
        return jsonify(response)
    else:
        return jsonify({'error': 'Request must be JSON'}), 400
