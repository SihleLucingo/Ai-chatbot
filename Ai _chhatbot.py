from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
chatbot = ChatBot('MyChatBot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')
while True:
    try:
        user_input = input("You: ")
        response = chatbot.get_response(user_input)
        print(f"ChatBot: {response}")

    except (KeyboardInterrupt, EOFError, SystemExit):
        break
