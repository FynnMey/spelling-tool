import google.generativeai as genai
apiPrivateKey = 'AIzaSyB-NySLmTA3tXcThrO-8lHt4leUb6NpKfM'

genai.configure(api_key=apiPrivateKey)
model = genai.GenerativeModel("gemini-1.5-flash")


def googleGeminiRequest(t):
    params = 'Bitte behebe in folgendem Sazt Saztbau und Rechtschreibfehler und gibt ihn mir wieder zurück: '
    response = model.generate_content(params + t)
    if (response.text):
        return response.text
    else:
        return '500'