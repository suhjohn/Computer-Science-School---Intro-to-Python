from DataHandler import *

#전체 학년 평균 : 50점

dh = DataHandler('class_1.xlsx', '2-3')
#dh = DataHandler('class_1.dat', '2-3')
dh.get_evaluation(50)

print("the lowest score : ({}: {})".format(
    dh.who_is_lowest(), dh.get_lowest_score()))

print("the highest score : ({}: {})".format(
    dh.who_is_highest(), dh.get_highest_score()))