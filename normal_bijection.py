def equation(x):
	return (x - 300) * (x + 4000) * (x - 50)

count = 0
x1 = int(raw_input("Please enter x1 such that eqn > 0 :")) 
x2 = int(raw_input("Please enter x1 such that eqn < 0 :"))
flag = True
while(flag):
	count += 1
	newx = 0.5 * (x1 + x2)
	fofx = equation(newx)
	print newx
	if fofx > 0: x1 = newx
	if fofx < 0: x2 = newx
	#print "abs " +  str(fofx)
	if abs(fofx) < 1: 
		flag = False
print count