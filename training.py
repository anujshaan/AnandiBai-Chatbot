from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

try:
	os.remove("db.sqlite3")
	print("Old database removed. Training new database")
except:
	print('No database found. Creating new database.')

eng_med_bot = ChatBot('Bot')
eng_med_bot.set_trainer(ListTrainer)
for file in os.listdir('data'):
        print('Training using '+file)
        convData = open('data/' + file).readlines()
        eng_med_bot.train(convData)
        print("Training completed for "+file)
    

