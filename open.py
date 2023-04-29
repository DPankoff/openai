import openai
import gradio as gr

# create key by txt
openai.api_key = open("key.txt", "r").read().strip('\n')


message_history = [{"role":"user", "content": f"Joke"},
                   {"role": "assistant", "content": f"OK"}]


def predict(input):
    global message_history
    
    message_history.append({"role": "user", "content": input})
    comletion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = message_history,
    )

    reply = comletion.choices[0].message.content
    print(reply)
    message_history.append({"role": "assistant", "content" : reply})

    response = [(message_history[i]["content"], message_history[i+1]["content"]) for i in range(2, len(message_history) - 1, 2) ]
    return response


with gr.Blocks() as demo:
    
    chatbot = gr.Chatbot()
    with gr.Row():
        txt = gr.Textbox(show_label = False, placeholder = "Введите сообщение ...").style(containter = False)
        txt.submit(predict, txt, chatbot)
        txt.submit(None, None, txt, _js="() => {''}")
        
demo.launch()
