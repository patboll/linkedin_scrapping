import openai

API_KEY = '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'
openai.api_key = API_KEY

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "What is the difference between Celsius and Fahrenheit?"}
    ]
)
print(response)
