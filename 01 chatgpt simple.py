import openai

openai.api_key= "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give me 3 ideas for apps could build with openai apis"}])
print(completion.choices[0].message.content)