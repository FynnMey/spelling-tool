from backendServer import app
from googleGemini import googleGeminiRequest

googleGeminiRequest('Behebe die rechtschreibfehler und gebe in einem json wieder welche wörter falsch sind. "Hiar steht eins super lange text"')
app.run(debug=True)