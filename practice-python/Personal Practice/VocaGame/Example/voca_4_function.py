#영단어 퀴즈 프로그램 함수 부분

import time
import random
from openpyxl import *


class VocaReader():
	#클래스 메서드
	#클래스 초기화 전에 미리 파일을 읽어들이는 역할
	@classmethod
	def get_data_from_excel(cls, filename):
		en_voca = []
		kr_voca = []
		en_sent = []
		kr_sent = []

		wb = load_workbook(filename)
		ws = wb.active
		g = ws.columns
		en_v = next(g)
		kr_v = next(g)
		en_s = next(g)
		kr_s = next(g)

		for key in en_v:
			en_voca.append(key.value)

		for key in kr_v:
			kr_voca.append(key.value)

		for key in en_s:
			en_sent.append(key.value)

		for key in kr_s:
			kr_sent.append(key.value)

		return en_voca, kr_voca, en_sent, kr_sent
		
	def __init__(self, filename):
		#클래스 초기화
		#클래스 메서드 읽어들이고
		#캐시 선언 
		self.rawdata = VocaReader.get_data_from_excel(filename)
		self.cache = {}

	def get_unpack(self):
		#언패킹 함수
		#rawdata를 언패킹해서 영단어, 한글 뜻, 영어 예문, 한글 번역으로 나눔
		if 'unpack' not in self.cache:
			en_v, kr_v, en_s, kr_s = self.rawdata
			self.cache['unpack'] = en_v, kr_v, en_s, kr_s

		return self.cache.get('unpack')

	def get_select_list(self, start_num):
		#사용자가 입력한 번호부터 시작하도록 리스트를 자르는 함수
		if 'select_list' not in self.cache:
			en_v, kr_v, en_s, kr_s = self.get_unpack()

			en_v = en_v[start_num -1 : start_num + 14]
			kr_v = kr_v[start_num -1 : start_num + 14]
			en_s = en_s[start_num -1 : start_num + 14]
			kr_s = kr_s[start_num -1 : start_num + 14]
			
			self.cache['select_list'] = en_v, kr_v, en_s, kr_s

		return self.cache.get('select_list')

	def get_random_list(self,start_num):
		#잘라낸 리스트를 랜덤으로 뒤섞는 함수
		if 'random_list' not in self.cache:
			en_v, kr_v, en_s, kr_s = self.get_select_list(start_num)

			ans_list = list(range(len(en_v)))
			ans_num = random.sample(ans_list,len(ans_list))

			en_v = list(map(lambda x: en_v[x], ans_num))
			kr_v = list(map(lambda x: kr_v[x], ans_num))
			en_s = list(map(lambda x: en_s[x], ans_num))
			kr_s = list(map(lambda x: kr_s[x], ans_num))

			self.cache['random_list'] = en_v, kr_v, en_s, kr_s

		return self.cache.get('random_list')

#여기까진 데이터를 읽어들이는 함수였고
#이제부터는 게임플레이 함수입니다

	def introduce(self,user_name):
		#사용자에게 시작번호를 받는 함수
		raw_list = self.get_unpack()
		en_v, kr_v, en_s, kr_s = raw_list
		how_long = len(en_v)

		start = ''
		while start == '':
			try:
				start = int(input("\nVoca Quiz!\nWe have " + str(how_long) + " words.\
				\nPress the start number, " + str(user_name) + ".\nThen we'll test 15 words. : "))
				if start + 14 > how_long:
					start = ''
					print ("\nYou typed too big number! Try again.")
					continue
				if start == 0:
					start = ''
					print ("\nYou typed too low number! Try again.")
					continue
			except ValueError:
				print("\nWrong typed. Try again.")
			else:
				print("\nAfter 3 seconds, the game will begin!\nPlease wait...")
				time.sleep(3)

		return start

	def good_bye(self, user_name, wrong_ans):
		#퀴즈가 끝나고 결과를 알려주는 함수
		if wrong_ans == []:
			print("ALL CORRECT! YOU ARE VOCA MASTER!!")
		else:
			print("In this quiz, you failed this: \n")
			print(wrong_ans)

		print("\nGood Job! " + str(user_name) + "! See you next time!")



