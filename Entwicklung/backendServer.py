from flask import Flask, jsonify, request, render_template, send_from_directory
from googleGemini import googleGeminiRequest
from flask_cors import CORS
import os

app = Flask(
    __name__,
    template_folder='website/dist/spa',
    static_folder='website/dist/spa/assets',  # Beibehalten des 'assets'-Ordners für andere Dateien
)

CORS(app)

# Route für statische Dateien im Hauptverzeichnis von 'dist/spa'
@app.route('/<path:filename>')
def serve_static_file(filename):
    return send_from_directory('website/dist/spa', filename)

# Standardseite
@app.route('/')
def home():
    return render_template('index.html')

# Andere Routen (beibehalten)
@app.route('/api/check-text', methods=['POST'])
def api():
    data = request.get_json()
    message = data.get('message', 'Kein Text übergeben')
    geminiResponse = googleGeminiRequest(message)
    print(geminiResponse)
    try:
        return geminiResponse
    except():
        return 'Unerwateter Fehler'

if __name__ == '__main__':
    app.run(debug=True)