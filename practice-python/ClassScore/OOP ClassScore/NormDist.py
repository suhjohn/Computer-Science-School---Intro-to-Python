#Standard_Deviation Library
#Three methods: Avg, Var, NormDist


from functools import reduce
import math

class NormDist:
	#the reason why we do not need members is because we just have methods in the class. There's default init that's made if we don't put anything.
	def average(self, scores):
		return reduce(lambda a, b: a + b, scores)/len(scores)

	def variance(self, scores, avrg):
		return round(reduce(lambda a, b: a + b, 
			map(lambda s: (s-avrg)**2,scores))/len(scores), 1)

	def std_dev(self, variance):
	 	return round(math.sqrt(variance), 1)
