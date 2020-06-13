from flask import Flask
from chatbot import chatbot
from chatterbot.trainers import ListTrainer
# need to import the notebook conversations here
# or create a conversations.py file
import conversations.py


@app.route('/')
def index():
    return "hello world"


@app.route('/predict', methods=['POST'])
def make_prediction():

    #chatterbot.trainers.ListTrainer(chatbot, **kwargs)[source]
    # Allows a chat bot to be trained using a list of strings where the list represents a conversation.
    app = Flask(__name__)
    trainer = ListTrainer(chatbot)
    # Replace with movie conversations here????
    trainer.train([
        conversations
    ])

    data = request.get_json()
    return "you posted {0}".format(data['message'])


if __name__ == "__main__":
    app.run(host='0.0.0.0')
