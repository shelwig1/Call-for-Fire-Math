import string

class mgrs:
	alphabet = string.ascii_uppercase	
	validGZD = [[(each + str(number))for number in range(1,61)] for each in alphabet]


	def __init__(self, gzd, thousandkmID, grid):
	gzd = self.gzd
	thousandkmID = self.thousandkmID
	grid = self.grid

#valid coords for gzd are A01 Z60
#thousandkmID AA to ZZ
# 00000,00000 to 99999,99999

#we can make the overflow method generic to handle different values, not terrible here

#test cases