import random

random_number = random.randint(1,20)
print(random_number)

while True:
    guess = input("Guess the number: ")

    if guess.isdigit():
        
        guess = int(guess)

        if (guess == random_number):
            print("That's Correct")
            break
        
        else:
            print("That's Wrong")

    else:
        print("That's not a digit")

    
