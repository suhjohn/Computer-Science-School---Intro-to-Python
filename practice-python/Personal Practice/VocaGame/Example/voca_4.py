#영단어 퀴즈 프로그램 실행 부분

import time
import random
from openpyxl import *
from voca_4_function import *


if __name__ == "__main__":
	voca = VocaReader('voca_1500_1599.xlsx')
	#엑셀 파일을 로드합니다
	user_name = input("Hi, What's your name?: ")
	#인풋 함수로 이름을 받습니다
	start_num = voca.introduce(user_name)
	#introduce함수로 user_name을 보내고 시작번호를 받습니다
	random = voca.get_random_list(start_num)
	#시작번호를 함수로 넘겨서 최종 리스트를 넘겨받습니다
	en_v, kr_v, en_s, kr_s = random
	wrong_ans = []
	
	#for 루프: 추출한 영단어 리스트를 하나씩 돌리면서
	#사용자에게 정답을 입력받습니다
	for i in kr_v:
		num = kr_v.index(i)
		answer = en_v[num]
		blanks = '_ ' * len(answer)

		print("\nNo. ", num + 1)
		print(i)
		print("\n",blanks,"\n")
		print(en_s[num])
		print(kr_s[num])

		guess = str(input("\nType the answer.\n(If you want to quit, press 'q') :"))
		if guess == 'q':
			print("\nOK, see you next time!\n")
			break
		
		elif guess == answer:
			print("\n<Congratuation!> The answer is\n" + answer, "\n" + i, "\n")
			time.sleep(2)
		
		else:
			wrong_ans.append(answer)
			print("\n<Wrong!> The answer is\n" + answer + "\n", i, "\n")
			time.sleep(2)
	
	#게임이 끝나면 굿바이 함수를 출력하고 끝납니다
	voca.good_bye(user_name, wrong_ans)


	

	