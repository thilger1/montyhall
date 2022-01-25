import random

def switch(n):
    wins = 0
    loses = 0
    for i in range(n):

        car = random.randint(1,3)
        choice = random.randint(1,3)
        #if you chose correctly initially, you would switch to the incorrect door
        if car == choice:
            loses += 1

        #if you chose incorrectly initially, Monty would remove the other incorrect door and you would switch to the correct door
        if car != choice:
            wins += 1
    print('Switch')
    print('Win percentage: ' + str(int(wins / n * 100)) + '%')
    print('Loss percentage: ' + str(int(loses /n * 100)) + '%')

def stay(n):
    wins = 0
    loses = 0
    for i in range(n):

        car = random.randint(1,3)
        choice = random.randint(1,3)
        #if you chose correctly initially, you would stay on the correct door
        if car == choice:
            wins += 1

        #if you chose incorrectly initially, you would not switch and lose
        if car != choice:
            
            loses += 1
    print('Stay')
    print('Win percentage: ' + str(int(wins / n * 100)) + '%')
    print('Loss percentage: ' + str(int(loses / n * 100)) + '%')

#running both strategies a million times
switch(1000000)
stay(1000000)
