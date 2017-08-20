from openpyxl import *
from normal_dist import * 

def get_rawdata_from_excel(filename):
	'''
	get_rawdata_from_excel(filename). - dict of rawdata
	read an excel file and return {'name' : 'score'',...}
	'''
	wb = load_workbook(filename)
	ws = wb.active
	raw_data = {}
	g = ws.rows
	
	for name, score in g: 
		raw_data.update({name.value : score.value})
	return raw_data

def evaluateClass(avrg, total_avrg, standard_deviation):
	if avrg <total_avrg and standard_deviation >20:
		print("Grade below avg, big diff in students.")
	elif avrg >total_avrg and standard_deviation >20:
        		print("Grade above avg, big diff in students. Careful!")
	elif avrg < total_avrg and standard_deviation <20:
		print("Small diff in students, but Grade below avg. Careful!")
	elif avrg > total_avrg and standard_deviation <20:
		print("Grade above avg, small diff in students.")

# if executing this file as main : execute below if
# else if imported as a module : do not execute below if 
# When library : written as test code 
if __name__ == "__main__":
	excel_file = input("input an excel file : ")
	raw_data = get_rawdata_from_excel(excel_file)
	scores = list(raw_data.values())
	avrg = average(scores)
	variance = variance(scores)
	standard_deviation = standard_deviation(scores)
	print("average {0}, variance : {1}, standard deviation : {2}".format
	(avrg, variance, standard_deviation))
	evaluateClass(avrg, 50, standard_deviation)

