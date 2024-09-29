"""Naruto: Shinobi Quest Version 1
This is the initial main program where
program will be prepared before splitting into modules"""

#imports
import random

#create dictionaries

roles ={
    'Naruto':{
        'Summon': 2,
        'Ninjutsu': 2,
        'Genjutsu': -1,
        'Intelligence': 0
    
    },
    'Sasuke':{
        'Summon': 0,
        'Ninjutsu': 1,
        'Genjutsu': 2,
        'Intelligence': 2
    }
}

resultThresholds ={
    'Critical Loss': (1,3),
    'Loss': (4,7),
    'Win': (8,10),
    'Critical Win': (11,14)
}

questChallenges ={
    ('Defeat Reanimated Shinobi', 'Summon'),
    ('Defeat Kabuto', 'Intelligence'),
    ('Defeat Obito', 'Genjutsu'),
    ('Defeat Madara', 'Ninjutsu')
}
#define functions
def diceRoll():
    
    #random roll of two dices that each can give a number from 1-6, meaning lowest result possible is 2 and highest is 12
    diceResult = random.randint(2,12)
    
    return diceResult

def challengeResult():
    roll = diceRoll()
    for thresholdResult, (low,high) in resultThresholds.items():
        if low <= roll <= high:
           return thresholdResult
  
  


  

    

#1. Print a welcome message to the user and provide a short overview of the game including it's name and goal

#2. Give user choice of character

#3. Present quest challenges one at a time



#4. After all challenges, display win or loss message to user
