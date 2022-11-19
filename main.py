from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Test')
conv = open(r"D:\pycharmfolder\Chats").readlines()

trainer = ListTrainer(bot)
trainer.train(conv)

while True:
   request = input('you : ')
   response = bot.get_response(request)
   print ("Bot :", response)