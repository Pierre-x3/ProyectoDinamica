from chatterbot import ChatBot

chatbot = ChatBot(
    'CoronaBot'
)


from chatterbot.trainers import ListTrainer

trainer = ListTrainer(chatbot)

training_data_quesans = open('covid.txt', encoding='utf8').read().splitlines()
training_data_personal = open('conversacion.txt', encoding='utf8').read().splitlines()

training_data = training_data_quesans + training_data_personal

trainer.train(training_data)


from chatterbot.trainers import ChatterBotCorpusTrainer

trainer_corpus = ChatterBotCorpusTrainer(chatbot)

trainer_corpus.train(
    'chatterbot.corpus.spanish'
)
