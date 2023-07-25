import random
from guessart import logo



# easy level


def easy():
    global attempt_easy
    attempt_easy=10
    guess=random.randint(1,101)
    print(f"You have {attempt_easy} attempts")
    user_choice=int(input("Make a guess: "))
    while (user_choice!=guess and attempt_easy>1):
        
        if(user_choice>guess):
            print("Too High!")
            attempt_easy-=1
            print(f"you have {attempt_easy} attempts left")
            user_choice=int(input("Guess again: "))
        else:
            print("Too Low!")
            attempt_easy-=1
            print(f"you have {attempt_easy} attempts left")
            user_choice=int(input("Make a guess: "))
    if user_choice == guess:
        print("Congratulations! You guessed the correct number.")
    else:
        print(f"Sorry, you ran out of attempts. The correct number was {guess}.")
            
 #hard level           
def hard():
    global attempt_hard
    attempt_hard=5
    guess=random.randint(1,101)
    print(f"You have {attempt_hard} attempts")
    user_choice=int(input("Make a guess: "))
    while (user_choice!=guess and attempt_hard>1):
       
        if(user_choice>guess):
            print("Too High!")
            attempt_hard-=1
            print(f"you have {attempt_hard} attempts left")
            user_choice=int(input("Guess again: "))
        else:
            print("Too Low!")
            attempt_hard-=1
            print(f"you have {attempt_hard} attempts left")
            user_choice=int(input("Make a guess: "))
    if user_choice == guess:
        print("Congratulations! You guessed the correct number.")
    else:
        print(f"Sorry, you ran out of attempts. The correct number was {guess}.")
print(logo)            
print("Welcome to the number guessing game!")

print("I'm guessing a number between 1-100: ")

choice= input("Choose Difficulty level: 'easy' or 'hard': " )
if choice=='easy':
    
    easy()

if choice=='hard':
    
    hard()







