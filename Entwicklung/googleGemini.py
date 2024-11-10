import google.generativeai as genai
apiPrivateKey = 'AIzaSyB-NySLmTA3tXcThrO-8lHt4leUb6NpKfM'

genai.configure(api_key=apiPrivateKey)
model = genai.GenerativeModel("gemini-1.5-flash")


def googleGeminiRequest(t):
    response = model.generate_content(t)
    if (response.text):
        print(response.text)
    else:
        print('zgsda')