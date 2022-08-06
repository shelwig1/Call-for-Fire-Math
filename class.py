class polarshift:
#accepts an MGRS object, outputs an MGRS object


#where should adding stuff to MGRS happen?
#should happen within the object

#determine shift in enemyPosition, add the shift within the MGRS object

#Mils vs degrees
#jesus fuck we still don't have MGRS enabled

#what happens when our numbers exceed the appropriate values


	def __init__(self, grid, direction, distance):
		self.grid = grid
		self.direction = direction
		self.distance = distance

	def polar2cartesian(grid,direction,distance):
		rads = math.radians(direction)

		x = round(distance * math.cos(rads))
		y = round(distance * math.sin(rads))

		grid[0] += x
		grid[1] += y

		return (grid)

	def output(grid, precision):
		return [str(s).zfill(precision) for s in grid]

