from HangmanExecution import *


class Hangman:
	HangmanExecution = HangmanExecution()

	def opening_selection(self):
		opening_selection = input("Welcome to Hangman! \
		\n---------------------------------------\
		\nPlay                       Scoreboard\
		\nHelp                       Exit\
		\n---------------------------------------\
		\nType which depth you want to go...")
		return opening_selection
	def hangman(self):
		opening_selection = self.opening_selection()
		if opening_selection.lower() == "play":
			while True:
				self.HangmanExecution.hangman_game()
				continue_or_not = input("Would you like to play again? Y / N  ")
				if continue_or_not.lower() == "y":
					continue
				elif continue_or_not.lower() == "n":
					menu_or_exit = input("Would you like to return to the main menu or exit? Menu / Exit  ")
					if menu_or_exit.lower() == "menu":
						return self.hangman()
					elif menu_or_exit.lower() == "exit":
						return 
					else:
						print("Error: Not a valid keyword.")
						continue
				else:
					print("Error: Not a valid keyword.")
	
	
		elif opening_selection.lower() == "scoreboard":
			self.HangmanExecution.scoreboard()
		elif opening_selection.lower() == "help":
			pass
		elif opening_selection.lower() == "exit":
			return
		else:
			print("Error: Not a valid keyword.\n\n")
			self.hangman()
	

if __name__ == '__main__':
	hangman = Hangman()
	hangman.hangman()

