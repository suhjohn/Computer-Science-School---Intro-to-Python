import math
from openpyxl import *
from functools import reduce

#Read data from file and create data structure
wb = load_workbook('class_1.xlsx')

#Activate a certain worksheet, in this case just a worksheet
ws = wb.active

#{'name' : score, 'name' : score}
raw_data = {}
g = ws.rows
for c1, c2 in g: 
	raw_data.update({c1.value : c2.value})

scores = []
for score in raw_data.values():
	scores.append(score)
#avg
avg = reduce(lambda a, b: a + b , scores) / len(scores)

#var
var = round(reduce(lambda a, b: a + b,
	map(lambda s: (s - avg) ** 2 / len(scores), scores)), 1)

#stdv
standard_deviation = round(math.sqrt(var), 1)

print(
    "평균 :{0}, 분산 : {1}, 표준 편차 : {2}".format(
    avg, var, standard_deviation))

if avrg <50 and standard_deviation >20:
    print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.")
elif avrg > 50 and standard_deviation >20:
    print("성적은 평균이상이지만 학생들 실력 차이가 크다. 주의 요망!")
elif avrg < 50 and standard_deviation <20:
    print("학생들간 실력차는 나지 않으나 성적이 너무 저조하다. 주의 요망!")
elif avrg > 50 and standard_deviation <20:
    print("성적도 평균 이상이고 학생들의 실력차도 크지 않다.")


