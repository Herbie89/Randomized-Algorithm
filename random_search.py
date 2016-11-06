from random import randint

lista = range(1, 1000)
listb = []
x = 149
countflag  = True
number = 0
while(countflag):
	flag = True
	number += 1
	if number == 20: countflag = False
	count = 0
	while flag:
		count += 1
		temprand = randint(1, 1000)
		if temprand == x:
			flag = False
	listb.append(count)
	#print count
#print listb

print("We are trying to search a number between 1 to 1000 here!")
print("The different number of times each search took was :")
suma = 0 
for item in listb:
	suma += item
	print item
#print("So on an average it takes " + str(suma/len(listb)) + " number of times")




# Output
# E:\Current_Projects\Robotics>python random_search.py
# 69

# E:\Current_Projects\Robotics>python random_search.py
# 2280

# E:\Current_Projects\Robotics>python random_search.py
# 1182

# E:\Current_Projects\Robotics>python random_search.py
# 436

# E:\Current_Projects\Robotics>python random_search.py
# 1779

# E:\Current_Projects\Robotics>python random_search.py
# 10

# E:\Current_Projects\Robotics>python random_search.py
# 3

# E:\Current_Projects\Robotics>python random_search.py
# 495

# E:\Current_Projects\Robotics>python random_search.py
# 875

# E:\Current_Projects\Robotics>python random_search.py
# 3857

# E:\Current_Projects\Robotics>python random_search.py
# 1548

# E:\Current_Projects\Robotics>python random_search.py
# 569

# E:\Current_Projects\Robotics>python random_search.py
# 923

# E:\Current_Projects\Robotics>python random_search.py
# 364

# E:\Current_Projects\Robotics>python random_search.py
# 695

# E:\Current_Projects\Robotics>python random_search.py
# 755

# E:\Current_Projects\Robotics>python random_search.py
# 670

# E:\Current_Projects\Robotics>python random_search.py
# 1060

# E:\Current_Projects\Robotics>python random_search.py
# 329

# E:\Current_Projects\Robotics>python random_search.py
# 54

# E:\Current_Projects\Robotics>python random_search.py
# 415