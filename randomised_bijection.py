from random import randint

def equation(x):
	#return (x - 300) * (x + 4000) * (x - 50)
	return x - 10


count = 0
bool1, bool2 = True, True
while(bool1 or bool2):
	count += 1
	temprand = randint(-10000, 10000)	
	if equation(temprand) < 0:
		x2 = temprand
		bool2 = False
	if equation(temprand) > 0:
		x1 = temprand
		bool1 = False

flag = True
while(flag):
	count += 1
	if x1 > x2 : newx = randint(x2, x1)
	else: newx = randint(x1, x2)
	fofx = equation(newx)
	print newx
	if fofx > 0: x1 = newx
	if fofx < 0: x2 = newx
	if fofx == 0: 
		flag = False
print count