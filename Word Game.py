import random
import json

def wordgame():
    with open('C:\\Users\\Isaac\\PIN Bootcamp\\words.txt', mode = 'r') as my_words:
        word_list = [line.split(',') for line in my_words.read().splitlines()]

    #data = json.load(open("C:\\Users\\Isaac\\PIN Bootcamp\\data.json"))  

    while True:
        print("Are you ready to play the word game? input 'yes' to continue or 'no' to terminate" )
        ans = input().lower()
        if ans == 'yes':
            print("Welcome to the word game\n Here is how the game works:\n The Program generates a random word in an unorganized manner.\n Your task is to form a meaningful word with the word generated\n")
            #generate random word
            random_word = random.choice(word_list)
            print(random_word[0])            

            #change random word to list
            random_word_list = list(random_word[0])

            #shuffle the list
            random.shuffle(random_word_list)

            #join the shuffled list to form a single word
            shuffle_word = ''.join(random_word_list)

            point = 0

            while True:
                print(f'The word is: {shuffle_word}')  
                print("Rearrange the word above to give a meaningful word")
                word = input().lower()

                if word == random_word[0]:
                    print("That's right!")
                    point +=  len(random_word[0])
                    print (f"Your points: {point} points")
                    break
                else:
                    print("Oops, that's incorrect!")   

        elif ans == 'no':
            print("Thanks for visiting. Game terminated")
            break
        else:
            print("You've provided a wrong answer")

wordgame()


