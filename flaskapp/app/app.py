from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer


app = Flask(__name__)

bot = Chatbot('Echo')

trainer = ListTrainer(bot)
trainer.train(['what is your name?', 'My name is Echo'])
trainer.train(['who are you?', 'I am a BOT'])

trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')

@app.route('/')
def index():
    greeting = "hello world"
    return render_template('home.html', greeting = greeting)

@app.route('/predict', methods=['POST'])
def chatbot_response():
    data = request.get_json()
    print('you posted {0}'.format(data['entry']))
    return jsonify(response='What?!')

if __name__ == "__main__":
    app.run(host = '0.0.0.0')
    
    