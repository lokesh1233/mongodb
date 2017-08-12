import chatterbot


from chatterbot import ChatBot

chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        "chatterbot.logic.BestMatch"
    ],
)

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")


def chatbotResponse(msg):
    return chatbot.get_response(msg)

# Get a response to an input statement
#print(chatbot.get_response("Hello, how are you today?"))