from flask import Flask, jsonify, request, render_template

app = Flask(
    __name__,
    template_folder='website/dist/spa',
    static_folder='website/dist/spa/assets'
)

# Route für die Standardseite
@app.route('/')
def home():
    return render_template('index.html')

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

if __name__ == '__main__':
    app.run(debug=True)
