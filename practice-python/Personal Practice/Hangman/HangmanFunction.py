class HangmanFunction:
	
	# check if you got the word
	def is_word_guessed(self, secret_word, letters_guessed):
		set_secret_word = set(secret_word)
		set_letters_guessed = set(letters_guessed)
		common_set = set_secret_word & set_letters_guessed
		return set_secret_word == common_set

	# return the guessed word so far. apple - _ p p _ _
	def get_guessed_word(self, secret_word, letters_guessed):
		word = ""
		for i in range(len(secret_word)):
			if secret_word[i] in letters_guessed:
	 			word += secret_word[i] + " "
			else:
       				word += "_ "
		return word	

	# return alphabets you have left
	def get_available_letters(self, letters_guessed):
		alphabets = "abcdefghijklmnopqrstuvwxyz"
		new_alphabets = ""
		for i in range(len(alphabets)):
			if alphabets[i] in letters_guessed:
				new_alphabets += "_ "
			else:
				new_alphabets += alphabets[i]
		return new_alphabets

	"""
	return if the word that I've guessed so far, my_word (ex. _ p p _ _ ) 
	match a word i(ex. o p p s e)
	"""
	def match_with_gaps(self, my_word, other_word):
		my_word_without_gaps = my_word.replace(" ", "")
		if len(my_word_without_gaps) != len(other_word):
			return False
		for i in range(0, len(my_word_without_gaps) - 1):
			if my_word_without_gaps[i].isalpha():
				if my_word_without_gaps[i] != other_word[i]:
					return False
				else:
					continue
		return True

	def show_possible_matches(self, my_word, wordlist):
		for word in wordlist:
			if self.match_with_gaps(my_word, word):
				print(word)



