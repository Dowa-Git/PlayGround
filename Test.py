import random

MaxGameCounter = 10
GameCounter = 0
EndCondition = False
WinCondition = False

while not EndCondition:
    if GameCounter > MaxGameCounter or WinCondition:
        InputGameMode = input('Try Again?')
        if InputGameMode == 'y':
            GameCounter = 0
            continue
        elif InputGameMode == 'n':
            print('See you soon')
            EndCondition = True
        else:
            print('Incorrect input, please inptu "y" or "n"')
            continue
    elif GameCounter == 0:
        RandomNumberList = random.sample([i for i in range(9)], 3)

    InputList = input('Input the numbers').split()
    Strike = 0
    Ball = 0
    Out = 0
    for i in range(3):
        if int(InputList[i]) in RandomNumberList:
            if int(InputList[i]) == RandomNumberList[i]:
                Strike += 1
                continue
            Ball += 1
        else:
            Out += 1
    print(f'Strike : [{Strike}] , Ball : [{Ball}], Out : [{Out}]')
    if Strike == 3:
        print('You Win!')
        WinCondition = True
    GameCounter+=1
    