#create a vocabulary guessing game
#open an excel file with premade data
#take in each rows that has vocab, Korean definition, english example, translated Korean example. 
#Add a function for the user to be able to create their own vocab card and quiz himself
#

class VocaGame:

	@classmethod
	def get_data_from_excel(cls, filename):
		voca_list = []
		wb = load_workbook(filename)
		ws = wb.active
		g = ws.rows

		keys = [word, kor_def, eng_ex, kor_ex]

		#Make lst = [{'word' : forever, 'kor_def' : ___, 'eng_ex' : _____, 'kor_ex' : _________}, {'word' : feed,...}...]
		for row in g:
			dic = {k : v.value for k, v in zip(keys, row)}
		voca_list.append(dic)

	def __init__()


