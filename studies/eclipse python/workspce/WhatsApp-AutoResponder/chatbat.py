from chatterbot import ChatBot

chatbot = ChatBot(
    'Lokesh',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
    #===========================================================================
    # logic_adapters=[
    #     'chatterbot.logic.MathematicalEvaluation',
    #     "chatterbot.logic.BestMatch"
    # ],
    #===========================================================================
)

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

#train custom
#chatbot.train("chatterbot.corpus.custom")

def chatbotResponse(msg):
    return chatbot.get_response(msg)

import time

while(1):
    messageVal='Hi'
    print(chatbot.get_response(messageVal))
    time.sleep(10)
    


# Get a response to an input statement
#print(chatbot.get_response("Hello, how are you today?"))