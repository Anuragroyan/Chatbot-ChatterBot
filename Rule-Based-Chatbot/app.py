from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

chatbot = ChatBot('Dungeon_master')

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get", methods=["GET","POST"])
def chatbot_response():
    msg = request.form["msg"]
    response = chatbot.get_response(msg)
    return str(response)


if __name__ == "__main__":
    app.run()             

