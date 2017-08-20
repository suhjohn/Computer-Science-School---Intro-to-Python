#반 성적 가져와서 
#연관된 모든 연산을 할 수 있어야 하고
#이 연산한 결과를 Caching
#NormDist Object inherit(IS-A) or 합성(HAS-A)
#Q1. class is IS-A or HAS-A?
#Q2. class member? or instance member? 
#does it need to be an individual object? or is it a "tool" that's applied to all objects?
# -*- coding:utf-8 -*-

from NormDist import *
from openpyxl import *
from functools import reduce

class DataHandler: 
	#create a class member evaluator
	evaluator = NormDist()

	#create a class method that creates a dictionary {'name': score...} from excel file
	@classmethod
	def get_data_from_excel(cls, filename):
		dic = {}
		wb = load_workbook(filename)
		ws = wb.active
		row = ws.rows

		for name, score in row:
			dic[name.value] = score.value
		return dic

	def __init__(self, filename, clsname):
		# From xlxs. receive data
		# {'name' : score, 'name', score}
		# 
		self.rawdata = DataHandler.get_data_from_excel(filename)
		self.clsname = clsname
		#가져온 데이터랑 필요할 때 마다 연산된 데이터(결과값)을 저장해 두는 역할 
		self.cache = {}

	#how to use cache
	def get_scores(self):
		if 'scores' not in self.cache:
			self.cache['scores'] = \
			list(self.rawdata.values())

		return self.cache['scores']

	def get_average(self):
		if 'average' not in self.cache:
			avg = \
			self.evaluator.average(self.get_scores())
			self.cache['average'] = avg
		return self.cache['average']

	def get_variance(self):
		if 'variance' not in self.cache:
			var = \
			self.evaluator.variance(self.get_scores(), self.get_average())
			self.cache['variance'] = var
		return self.cache['variance']

	def get_std_dev(self):
		if 'standard_deviation' not in self.cache:
			std_dev = \
			self.evaluator.std_dev(self.get_variance())
			self.cache['standard_deviation'] = std_dev
		return self.cache['standard_deviation']

	def who_is_highest(self):
		if "highest" not in self.cache:
			high = \
			reduce(lambda a, b: a if self.rawdata.get(a) > self.rawdata.get(b) else b, self.rawdata.keys())
			self.cache['highest'] = high
		return self.cache['highest']

	def get_highest_score(self):
		return self.rawdata[self.cache['highest']]

	def who_is_lowest(self):
		if "lowest" not in self.cache:
			low = \
			reduce(lambda a, b: a if self.rawdata.get(a) < self.rawdata.get(b) else b, self.rawdata.keys())
			self.cache['lowest'] = low
		return self.cache['lowest']

	def get_lowest_score(self):
		return self.rawdata[self.cache['lowest']]

	def get_evaluation(self, total_avrg):
	        print('*' * 50)
	        print("%s Class Score analysis result" % self.clsname)
	        print(
	        "Class {0}'s Average is {1}, Variance is {2},and therefore Standard Deviation is {3}".format(
	            self.clsname,
	            self.get_average(),
	            self.get_variance(),
	            self.get_std_dev()))
	        print('*' * 50)
	        print("%s class total evaluation" % self.clsname)
	        print('*' * 50)
	        self.evaluate_class(total_avrg)

	def evaluate_class(self, total_avrg):
		avrg = self.get_average()
		std_dev = self.get_std_dev()
		print(avrg)
		print(std_dev)
		print(total_avrg)
		if avrg <total_avrg and std_dev >20:
    			print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.")
		elif avrg > total_avrg and std_dev >20:
    			print("Grade above average but big difference in student's abilities. Be ware!")
		elif avrg < total_avrg and std_dev <20:
    			print("학생들간 실력차는 나지 않으나 성적이 너무 저조하다. 주의 요망!")
		elif avrg > total_avrg and std_dev <20:
    			print("성적도 평균 이상이고 학생들의 실력차도 크지 않다.")


