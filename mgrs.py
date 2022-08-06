import string

class mgrs:
	alphabet = string.ascii_uppercase	

	validGZDx = [str(number) for number in range(1,61)]
	validGZDy = [each for each in alphabet]

	validthousandx, validthousandy = [each for each in alphabet], [each for each in alphabet]

	validGridx, validGridy = [str(number) for number in range (0, 100000)], [str(number) for number in range (0, 100000)]  


	def __init__(self, gzd, thousandkm, grid):
		try:
			gzdX = validGZDx.index(gzd[0:1])
			gzdY = validGZDy.index(gzd[2])
			self.gzd = [gzdX,gzdY]
		except:
			print("Invalid grid zone designator.")

		try:
			thousandkmX = validthousandx.index(thousandkm[0])
			thousandkmY = validthousandy.index(thousandkm[1])
			self.thousandkm = [thousandkmX, thousandkmY]
		except:
			print("Invalid thousand kilometer ID")

		try:
			gridX = validGridx.index(grid[0])
			gridY = validGridy.index(grid[1])
			self.grid = [gridX, gridY]
		except:
			print("Invalid grid.")

	#ASSUMES YOU WILL ONLY ADJUST THROUGH THE GRID VARIABLE, NOT THE GZD OR THOUSANDKMID
	def addShift(xyshift):
		#takes an x and y shift array
		self.grid[0] += xyshift[0]
		self.grid[1] +=xyshift[1]
		correct()

		#we don't need to check for erros this way - we convert existing values
		#which are just indexes into actual numbers, then add what we need,
		#check if those numbers are valid and if not


		#we still need to do the same type of checks, fuck me

		#okay, check if new numbers are valid, and if not we still have to implement an
		#overflow deal