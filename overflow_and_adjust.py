vals = ['a','b','c']

x =["a", 0]
x[1] += 10

def overflow(x):
	increment = 0

	if x[1] > 9:
		while x[1] > 9:
			x[1] -= 10
			increment += 1

	elif x[1] < 0:
		while x[1] < 0:
			x[1] += 10
			increment -= 1

	handleLetter(x, increment)

def handleLetter(x, increment):
	try:
		index = vals.index(x[0])
		x[0] = vals[index + increment]
	except:
		print('tripped')
		x[0] = vals[-1]
		x[1] = 9

	return x

x =["a", 0]
print(handleLetter(x,5))

#now what does 2 letters look like?