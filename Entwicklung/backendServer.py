from flask import Flask, jsonify, request, render_template
from googleGemini import googleGeminiRequest

app = Flask(
    __name__,
    template_folder='website/dist/spa',
    static_folder='website/dist/spa/assets'
)

# Route für die Standardseite
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/check-text', methods=['POST'])
def api():
    data = request.get_json()

    message = data.get('message', 'Kein Text übergeben')
    geminiResponse = googleGeminiRequest(message)
    print(geminiResponse)

    return jsonify(geminiResponse)

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
