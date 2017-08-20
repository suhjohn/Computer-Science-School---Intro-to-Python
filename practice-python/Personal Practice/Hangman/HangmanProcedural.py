# Problem Set 2, hangman.py
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):

    set_secret_word = set(secret_word)
    set_letters_guessed = set(letters_guessed)
    
    return set_secret_word == set_letters_guessed

def get_guessed_word(secret_word, letters_guessed):

    word = ""
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            word += secret_word[i] + " "
        else:
            word += "_ "
    return word

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    new_alphabets = ""
    for i in range(len(alphabets)):
        if alphabets[i] in letters_guessed:
            new_alphabets += ""
        else:
            new_alphabets += alphabets[i]
    return new_alphabets

def hangman(secret_word):
    
    letters_guessed = []
    word_length = len(secret_word)
    incomplete_word = get_guessed_word(secret_word, letters_guessed)
    trial = 6
    warning = 3
    #start game
    print("aWelcome to the game Hangman!\
        \nI am thinking of a word that is {} letters long.\
        \nYou have {} warnings left.\
        \n---------------------------------------------------".format(word_length, warning))
    
    #when trial is not 0, warning is not 0 and the word is not guessed yet:
    while trial != 0 and warning != 0 and not is_word_guessed(secret_word, letters_guessed):

        a = input("You have {} guesses left.\
            \nAvailable letters: {}\
            \nPlease guess a letter : ".format(trial, \
                get_available_letters(letters_guessed))).lower()
        #if the input is not an alphabet
        if not a.isalpha():
            warning -= 1
            print("Your input is not an alphabet. \
                \nYou have {} warnings left. \
                \n{}\
                \n-----------------------------------------------".format(warning, get_guessed_word(secret_word, letters_guessed)))
            continue

        #if the user already guessed the alphabet
        if a in letters_guessed:
            trial -= 1

            print("Oops! You've already guessed that letter. You have {} trials left: {}\
                \n-----------------------------------------------".format(trial, get_guessed_word(secret_word, letters_guessed)))
        #if the alphabet is not in the word
        elif a not in secret_word:
            trial -= 1     
            letters_guessed.append(a)
            print("Oops! That letter is not in my word! You have {} trials left: {}\
                \n-----------------------------------------------".format(trial, get_guessed_word(secret_word, letters_guessed)))
        #if the alphabet is in the word
        else:
            letters_guessed.append(a)
            print ("Good guess: {}\
                \n-----------------------------------------------".format(get_guessed_word(secret_word, letters_guessed)))            
    
    total_score = trial * len(letters_guessed)
    if trial == 0 or warning == 0:
        print("You lost. \
            \nYour word was : {}".format(secret_word))
    else:
        print("Congratulations, you won! \
            \n Your total score for this game is : {}".format(total_score))


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)
# -----------------------------------
def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    for i in range(0, len(other_word)):
        if my_word[i].isalpha():
            if my_word[i] != other_word[i]:
                return False
                break
            else:
                pass
    return True

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    for word in wordlist:
        if match_with_gaps(my_word, word):
            print(word)

def hangman_with_hints(secret_word):

    #var
    letters_guessed = []
    word_length = len(secret_word)
    incomplete_word = get_guessed_word(secret_word, letters_guessed)
    trial = 6
    warning = 3
    
    #start game
    print("Welcome to the game Hangman!\
        \nI am thinking of a word that is {} letters long.\
        \nYou have {} warnings left.\
        \n---------------------------------------------------".format(word_length, warning))
    
    #when trial is not 0, warning is not 0 and the word is not guessed yet:
    while trial != 0 and warning != 0 and not is_word_guessed(secret_word, letters_guessed):

        a = input("You have {} guesses left.\
            \nAvailable letters: {}\
            \nPlease guess a letter : ".format(trial, \
                get_available_letters(letters_guessed))).lower()
        #if the input is not an alphabet

        if a == "*":
            show_possible_matches(get_guessed_word(secret_word,letters_guessed))
        elif not a.isalpha():
            warning -= 1
            print("Your input is not an alphabet. \
                \nYou have {} warnings left. \
                \n{}\
                \n-----------------------------------------------".format(warning, get_guessed_word(secret_word, letters_guessed)))
            continue

        #if the user already guessed the alphabet
        if a in letters_guessed:
            trial -= 1

            print("Oops! You've already guessed that letter. You have {} trials left: {}\
                \n-----------------------------------------------".format(trial, get_guessed_word(secret_word, letters_guessed)))
        #if the alphabet is not in the word
        elif a not in secret_word:
            trial -= 1    
            letters_guessed.append(a)
            print("Oops! That letter is not in my word! You have {} trials left: {}\
                \n-----------------------------------------------".format(trial, get_guessed_word(secret_word, letters_guessed)))
        #if the alphabet is in the word
        else:
            letters_guessed.append(a)
            print ("Good guess: {}\
                \n-----------------------------------------------".format(get_guessed_word(secret_word, letters_guessed)))            
    
    total_score = trial * len(letters_guessed)

    if trial == 0 or warning == 0:
        print("You lost. \
            \nYour word was : {}".format(secret_word))
    else:
        print("Congratulations, you won! \
            \n Your total score for this game is : {}".format(total_score))

if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    print(secret_word)
    #hangman(secret_word)
    hangman_with_hints(secret_word)
###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
