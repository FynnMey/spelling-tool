from backendServer import app
from googleGemini import googleGeminiRequest

googleGeminiRequest('Wie viele Einwohner hat Deutschland?')
app.run(debug=True)