import math

class KFilter:
	def __init__(self):
		self.mean = 0
		self.variance = 10000
		
	def gaussian(self, x):
		res = math.pow( math.e, 
			math.pow(-(x-self.mean), 2) / (2 * math.pow(self.variance, 2) ) )
			
		res *= 1 / math.sqrt(2 * math.pi * self.variance * self.variance )
		return res
		
	def update(self, m, v):
		self.mean = (v*self.mean + self.variance*m)/(self.variance + v)
		self.variance = 1/((1/self.variance) + (1/v))
		
	def predict(self, m, v):
		self.mean += m
		self.variance += v
		
	def print_state(self):
		print("Mu: {}\tVar: {}".format(self.mean, self.variance))
		
			
			
if __name__ == "__main__":
	kf = KFilter()
	measurements = [5, 6, 7, 9, 10]
	motions = [1,1,2,1,1]
	# print(kf.gaussian(3))
	for i in range(len(motions)):
                print("\niteration: {}".format(i))
                kf.update(measurements[i], 4)
                print("update: ", end='')
                kf.print_state()
                kf.predict(motions[i], 2)
                print("predict: ", end='')
                kf.print_state()
			
			
