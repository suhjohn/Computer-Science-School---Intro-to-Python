import random
import string
from HangmanFunction import *

class HangmanExecution:

	hangmanfunction = HangmanFunction()
	
	# load words - Class method	
	@classmethod
	def load_words(cls):
		print("Loading word list from file...")
		file = open("words.txt", 'r')
		line = file.readline()
		wordlist = line.split()
		print(" ", len(wordlist), "words loaded.")
		return wordlist
	@classmethod
	def choose_word(cls, wordlist):
		return random.choice(wordlist)
	
	# instance variable declaration
	def __init__(self):
		self.secret_word = None
		self.player_name = None
		self.trial_left = 0
		self.warning_left = 0
		self.letters_guessed = []
		self.game_score = 0
		self.total_score = 0
		self.name_score_pair = {self.player_name : self.total_score}
		self.wordlist = HangmanExecution.load_words()
	
	def set_secret_word(self):
		self.secret_word = HangmanExecution.choose_word(self.wordlist)

	def get_secret_word(self):
		return self.secret_word

	def set_player_name(self, player_name):
		self.player_name = player_name

	def get_player_name(self):
		return self.player_name

	def set_trial_left(self, trials):
		self.trial_left = trials

	def get_trial_left(self):
		return self.trial_left
	
	def set_warning_left(self, warnings):
		self.warning_left = warnings

	def get_warning_left(self):
		return self.warning_left

	def reset_letters_guessed(self):
		self.letters_guessed = []

	def set_game_score(self, trial_left, word_length):
		self.game_score = trial_left * word_length

	def get_game_score(self):
		return self.game_score

	def welcome_statement(self, word_length, warning_left):
		player_name = input("Welcome to the game Hangman! \
			\nPlease Enter your name : ")
		self.set_player_name(player_name)

		print("I am thinking of a word that is {} letters long.\
			\nYou have {} warnings left.\
			\n---------------------------------------------------".format(word_length, warning_left))						

	def input_alphabet(self):
		a = input("Please guess a letter : ")
		return a

	def check_input(self, a):
		if a == "*":
			self.hangmanfunction.show_possible_matches\
			(self.hangmanfunction.get_guessed_word(self.secret_word, self.letters_guessed), self.wordlist)
			print(self.hangmanfunction.get_guessed_word(self.secret_word, self.letters_guessed))
			return False
		elif a.isalpha() == False:
			self.warning_left -= 1
			print("Your input is not an alphabet. \
			\nYou have {} warnings left. \
			\n{}\
			\n-----------------------------------------------".format(self.warning_left, \
				self.hangmanfunction.get_guessed_word(self.secret_word, self.letters_guessed)))
			return False
		elif len(a) > 1:
			print("Please give an input that is a single alphabet. \
				\n-----------------------------------------------")
			return False
		else:
			return a

	def alphabet_in_word(self, a, secret_word, letters_guessed):

		# if already guessed the letter
		if a in letters_guessed:
			self.trial_left -= 1	
			print("Oops! You've already guessed that letter. You have {} trials left: {}\
			\n-----------------------------------------------".format\
			(self.trial_left, self.hangmanfunction.get_guessed_word(secret_word, self.letters_guessed)))
			#if the alphabet is not in the word

		elif a not in secret_word:
			self.trial_left -= 1    
			self.letters_guessed.append(a)
			print("Oops! That letter is not in my word! You have {} trials left: {}\
			\n-----------------------------------------------".format\
			(self.trial_left, self.hangmanfunction.get_guessed_word(secret_word, self.letters_guessed)))
		#if the alphabet is in the word
		else:
			self.letters_guessed.append(a)
			print ("Good guess: {}\
			\n-----------------------------------------------".format\
			(self.hangmanfunction.get_guessed_word(secret_word, self.letters_guessed)))            	

	def ending_statement(self, secret_word, game_score):
		if self.trial_left == 0 or self.warning_left == 0:
			print("You lost. \
				\nYour word was : {}".format(secret_word))
		else:

			print("Congratulations, you won! \
				\n Your total score for this game is : {}".format(game_score))		

	def hangman_game(self):

		self.set_trial_left(6)
		trial_left = self.get_trial_left()
	
		self.set_warning_left(3)
		warning_left = self.get_warning_left()
	
		self.set_secret_word()
		secret_word = self.get_secret_word()

		word_length = len(self.secret_word)

		print(self.secret_word)

		#welcome statement
		self.welcome_statement(word_length, warning_left)

		#gameplay
		while not self.hangmanfunction.is_word_guessed(self.secret_word, self.letters_guessed)  and \
			self.trial_left != 0 and self.warning_left != 0:
			print("You have {} guesses left. \
				\nAvailable letters: {}".format\
				(self.trial_left, self.hangmanfunction.get_available_letters(self.letters_guessed)))
			a = self.input_alphabet()
			if self.check_input(a) == False:
				continue 
			self.alphabet_in_word(a, self.secret_word, self.letters_guessed)

		game_score = self.set_game_score(self.trial_left, word_length)
		self.ending_statement(self.secret_word, self.game_score)
		self.reset_letters_guessed()

	def scoreboard(self):
		pass

if __name__=="__main__":
	hangman = HangmanExecution()
	hangman.hangman_game()
