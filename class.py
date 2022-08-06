class enemyPosition:
#Mils vs degrees
#jesus fuck we still don't have MGRS enabled

#what happens when our numbers exceed the appropriate values


	def __init__(self, grid, direction, distance):
		self.grid = grid
		self.direction = direction
		self.distance = distance

	def process(grid):
		precision = len(self.grid[0])
		formatted = [int(s) for s in self.grid]
		polar = polar2cartesian(formatted,self.direction,self.distance)
		print(output)

	def polar2cartesian(grid,direction,distance):
		rads = math.radians(direction)

		x = round(distance * math.cos(rads))
		y = round(distance * math.sin(rads))

		grid[0] += x
		grid[1] += y

		return (grid)

	def output(grid, precision):
		return [str(s).zfill(precision) for s in grid]

