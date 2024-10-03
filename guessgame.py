import time
import random        
class JogoAdivinhação:
    user_scores = []
    


    def inicio(self):
        print('Welcome to the guessing game ')
        print('Try to guess a number between 1 and 100\nThe difficult will determine the number of chances')
        (input('Press enter to start\n'))

    
    def difficulty(self):
        choose = int(input('Enter the  number of difficulty:\n1 - Easy: 10 chances\n2 - Medium: 5 chances\n3 - Hard: 3 chances\n'))
        dificuldades = {1:{'difficulty':'easy','chances': 10, 'attemps': 0},
                        2:{'difficulty': 'medium', 'chances': 5, 'attemps': 0},
                        3:{'difficulty':'hard', 'chances':3, 'attemps': 0}}
        return dificuldades[choose]
    

    def hint(self, user_guess:int, number:int):
        if user_guess>number:
            print(f'incorrect, the number is less than {user_guess}')
            return
        print(f'incorrect, the number is greater than {user_guess}')
        return


    def ranking(self, user_score:list[dict]):
        for i in user_score:
            print(f'in this game you guessed in {i['time']} seconds with {i['attemps']} attemps in {i['difficulty']} mode')
        
    

    def play(self):
        self.inicio()
        level = self.difficulty()
        print('starting...\n')
        number = random.randint(1,100)
        start = time.time()
        win = False
        while level['chances']>0:
            try:
                user_guess = int(input('Enter your guess: '))
                if user_guess >100 or user_guess<0:
                    raise ValueError
            except ValueError:
                print('Guess out of range')
            level['attemps'] +=1
            if user_guess == number:
                end = time.time()
                print(f'You took {end-start:.2f} seconds to guess correctly ')
                win = True
                break
            else:
                self.hint(user_guess, number)
                level['chances'] -= 1
                print(f'chances remaining: {level["chances"]}')
        self.user_scores.append({'difficulty':level['difficulty'], 'attemps':level['attemps'], 'time':end-start})
        if win:
           print('Congratulations, you won')
           print()
        else:
            print(f'Oh no, you lost, the number were {number}')
            print() 
        try:
            new_try = int(input('Do you want to play again? press 1 to yes, or 0 to end the game\n'))
        except ValueError:
            print('incorrect input')
        if new_try == 1:
            self.play()
        print('-'*80)
        print('here are the scores of your games ')
        self.ranking(self.user_scores)

        
            
                
        
            
                
        

        