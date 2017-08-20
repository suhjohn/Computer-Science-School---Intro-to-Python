#numguess 
from random import randint

#choose the random integer which is the answer
answer = randint(1,100)

numguessedited = 1
# get username
username = input("Hi there, what is your name?")
# capitalize username for the lazy people 
username_capitalize = username[0].upper() + username[1:]    

#ask for a guess
i = 0
original_tries = 7
tries_left = original_tries
for i in range(i, original_tries):
    # Make user input a number and make sure the number is an integer, not a !,@,# or a,b,c
    try:
        guess = eval(input("Hey, %s, guess the number between 1 and 100 - trial left : %d time(s) " % (username_capitalize, tries_left)))
    except (SyntaxError, NameError):
        print ("Wrong. What you typed is not an integer, you stupid.")

    # When correct
    if answer == guess:
        print("Correct! The answer was ", str(answer))
        break

    # When tries_left is greater than 0
    elif tries_left > 1:
        if answer < guess and abs(answer - guess) < 10:
            print("You're really close, but your guess is a bit too high!")
        elif answer > guess and abs(answer - guess) < 10:
            print("You're really close, but your guess is a bit too low!")
        elif answer < guess and abs(answer - guess) > 10:    
            print("Your guess is too high. Try again!")
        else:
            print("Your guess is too low. Try again!")

    # When tries_left = 0 
    else:
        print("You have failed. The answer was %d. Good luck next time :p" % (answer))
    tries_left = tries_left - 1
ju
