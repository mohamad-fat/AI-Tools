import gradio
import openai

openai.api_key= "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"
messages = [{"role": "system", "content": "You are a Programming specialist on C# and .Net with the highest IQ possible"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    return reply

demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="Programming Specialist")

demo.launch(share=True)