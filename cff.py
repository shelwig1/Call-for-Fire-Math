import math
import convert

#focus on quadrant 1 work
# 360 and or 0/6400
# 90/1600
# 180/3200
# 270/4800
# 


#list concatenation to generate appropriate grids

# !---degrees and mils ---!
CONSTANT = 0.05625
RANGE = 100
DIR = 45

#6, 8, 10 digit grid compatibility

currPos = ['00123','00456']

#accepting mils or degrees
#does python have a library for handling mils? May need to create one.
#accepting different lengths of coordinates
#properly implement MGRS - list concatenation
#take input of range and compass from outside this program - let it come from other inputs

#EASY WAY - take degrees or mils, but funnel them into the equation as mils

#The angle in degrees is equal to the mils (NATO) multiplied by 0.05625.

#HEY DOOFUS THIS ONLY WORKS FOR QUADRANT 1, NO?
def polar2cartesian(currPos,RANGE,DIR):
	rads = math.radians(DIR)

	x = RANGE * math.cos(rads)
	y = RANGE * math.sin(rads)

	return(x,y)

#polar2cartesian(currPos,RANGE,DIR)

#we can convert, now what?


#accept 6,8,10 digit grids and round off accordingly
#there will be no decimals - we need to round off

def process(currPos,RANGE,DIR):
	digits = {
		5 : 10,
		4 : 8,
		3 : 6
	}

	#prepare the data
	precision = digits[len(currPos[0])]
	formatted = [int(currPos[0]),int(currPos[1])]
	print (formatted)
	#process the new position
	val = polar2cartesian(formatted,RANGE,DIR)

	#then format the val with the proper position
	print(val)

	#return roundVal(val, currPos)

def roundVal(val, currPos):
	#check the specificity of the coordinates, round it off appropriately
	pass

process(currPos,RANGE,DIR)