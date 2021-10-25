from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from Python_Dependencies.GrabbingCreds import GrabingCreds

#TODO move these to a json or mysql data holder
#TODO if using sqlalchemy, connet it to a database with a list of responses
#TODO Will have to provide a class
# to grab the responses in a dictionry {name of table : [list of responses]}
"""
List of responses
"""
#region ListOfResponses
small_talk = [
    'Hi',
    'how do you do bitch?',
    'fuck thats sucks man! Im good!',
    'whats your name?',
    'IM THE GREAT KEVIN< RULER OF THIS LAND!'
]

math_talk=['Fuck I cant do math?!?!', 'FUCK YOU SMART ASS!']
math_talk_2= ['Can you help me study UwU!', 'Ive been a bad bot...']
#endregion

kevin_AI = ChatBot(name='KevinTheGreat', read_only=False,
                   logic_adapters=
                   [
                       'chatterbot.logic.MathematicalEvaluation',
                       'chatterbot.logic.BestMatch'
                   ])

#when sql is introcduced, this will loop through a dictionary and get the key value pairs to train on
list_trainer = ListTrainer(kevin_AI)
for item in (small_talk, math_talk, math_talk_2):
    list_trainer.train(item)

#TODO class for the discord implemenation
class Discord_Handler:
    def __init__(self):
        self.token = GrabingCreds().GrabCreds('discord', 'token')

print(Discord_Handler().token)
