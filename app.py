from flask import Flask, render_template, request
from groq import Groq
import os

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"{user_input}",
                }
            ],
            model="llama3-8b-8192",
        )
        assistant_reply = chat_completion.choices[0].message.content
        return render_template('index.html', user_input=user_input, assistant_reply=assistant_reply)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
