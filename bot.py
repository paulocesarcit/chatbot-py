from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('PY Bot')

conversation = ['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo', 'Qual seu filme favorito?', 'Vingadores']

trainer = ListTrainer(bot)
trainer.train(conversation)

while True:
    ask = input("Usuário: ")
    response = bot.get_response(ask)
    if float(response.confidence) > 0.5:
        print('PY Bot: ', response)
    else:
        print('PY Bot: Ainda não sei responder esta pergunta')