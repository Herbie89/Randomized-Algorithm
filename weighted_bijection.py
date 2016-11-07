def equation(x):
	return (x - 300) * (x + 4000) * (x - 50)

count = 0

x1 = float(raw_input("Please enter x1 such that eqn > 0 :")) 
x2 = float(raw_input("Please enter x1 such that eqn < 0 :"))
flag = True
while(flag):
	count += 1
	fofx1 = equation(x1)
	fofx2 = equation(x2)
	denom = abs(fofx1) + abs(fofx2)
	newx = ( abs(fofx1) / denom ) * x1 + ( abs(fofx2) / denom ) * x2
	print newx
	fofx = equation(newx)
	if abs(fofx) < 1: 
		flag = False
	if fofx > 0: x1 = newx
	if fofx < 0: x2 = newx
print count 