import time
import random
class JogoAdivinhação:
    user_score = []
    def __init__(self):
        self.number = random.randint(1,100)


    def inicio(self):
        print('Welcome to the guessing game ')
        print('Try to guess a number between 1 and 100\nThe difficult will give the number of chances')
        (input('Press enter to start\n'))

    
    def difficulty(self):
        choose = int(input('Enter the  number of difficulty:\n1 - Easy: 10 chances\n2 - Medium: 5 chances\n3 - Hard: 3 chances\n'))
        dificuldades = {1:{'difficulty':'easy','chances': 10, 'attemps': 0},
                        2:{'difficulty': 'medium', 'chances': 5, 'attemps': 0},
                        3:{'difficulty':'hard', 'chances':3, 'attemps': 0}}
        return dificuldades[choose]
    
    def hint(self, user_guess:int):
        if user_guess>self.number:
            print(f'incorrect, the number is less than {user_guess}')
            return
        print(f'incorrect, the number is greater than {user_guess}')
        return

    

    def play(self):
        self.inicio()
        level = self.difficulty()
        print('starting...\n')
        while level['chances']>0:
            try:
                user_guess = int(input('Enter your guess: '))
                if user_guess >100 or user_guess<0:
                    raise ValueError
            except ValueError:
                print('Guess out of range')
            level['attemps'] +=1
            if user_guess == self.number:
                break
            else:
                self.hint(user_guess)
                level['chances'] -= 1
                print(f'chances remaining: {level["chances"]}')
        self.user_score.append(level)
        

game = JogoAdivinhação()
game.play() 
            
                
        
            
                
        

        