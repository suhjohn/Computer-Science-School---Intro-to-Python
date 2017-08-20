import math
from functools import reduce
'''

'''
def average(data_list):
	avg = reduce(lambda a, b: a + b , data_list) / len(data_list)
	return avg

def variance(data_list):
	var = round(reduce(lambda a, b: a + b,
		map(lambda s: (s - average(data_list)) ** 2 / len(data_list), data_list)), 1)
	return var

def standard_deviation(data_list):
	stdv = round(math.sqrt(variance(data_list)), 1)
	return stdv