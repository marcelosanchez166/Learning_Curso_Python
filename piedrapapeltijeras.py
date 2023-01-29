import random

choice = ['rock','paper','scissor']

points = int(input('Enter number of game points: '))

ppoint = 0 # Player points
cpoint = 0 # computer points

while ppoint<points and cpoint<points:
    
    computer = random.choice(choice)
    player = input('Your choice: ')
    print('Computer choose: ', computer, '\n')
    if computer == player: print("It's a tie, we both choose", computer)
    elif(player in choice):
        if computer == 'rock':
            if player == 'paper': 
                print('You won a point!!, paper > rock ')
                ppoint+=1
            else:
                print('Computer won a point!!, rock > scissor')
                cpoint+=1
        if computer == 'scissor':
            if player == 'paper': 
                print('Computer won a point!!, scissor > paper ')
                cpoint+=1
            else:
                print('You won a point!!, rock > scissor')
                ppoint+=1
        if computer == 'paper':
            if player == 'rock': 
                print('Computer won a point!!, paper > rock ')
                cpoint+=1
            else:
                print('You won a point!!, scissor > paper')
                ppoint+=1                
                
    else: print("Please choose one from: 'rock', 'paper', or 'scissor'")     
    
    print("Player: ", ppoint, "Computer: ", cpoint, '\n')

if ppoint>cpoint: print("Congratulations, you won!!")
elif ppoint<cpoint: print("Oops, you lost!!")
else: print("It's a tie")