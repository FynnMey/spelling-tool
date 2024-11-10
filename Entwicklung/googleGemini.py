import google.generativeai as genai

apiPrivateKey = 'AIzaSyB-NySLmTA3tXcThrO-8lHt4leUb6NpKfM'

genai.configure(api_key=apiPrivateKey)

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(
    "Behebe rechtschreibfehler in Folgendem Text: Hall o ich bin Fynn und ich mahe rechtschrfeifehler")
print(response.text)