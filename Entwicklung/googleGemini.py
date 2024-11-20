import google.generativeai as genai
apiPrivateKey = 'AIzaSyB-NySLmTA3tXcThrO-8lHt4leUb6NpKfM'

genai.configure(api_key=apiPrivateKey)
model = genai.GenerativeModel("gemini-1.5-pro")


def googleGeminiRequest(t):
    params = 'Behebe alle Rechtschreib und Satzbaufehler in folgenden Text und gebe ihn mir wieder zurück, wenn der Text sinnlos ist, gib ihn einfach ohne ihn zu bearbeiten zurück: '
    response = model.generate_content(params + t)
    if (response.text):
        return response.text
    else:
        return '500'