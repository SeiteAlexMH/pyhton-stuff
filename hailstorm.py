#hailstorm.py
#Alexandre Seite

def hailstorm(number):
	saved_number = number
	count = 0
	while number > 1:
		print(number)
		count += 1
		if number %2 == 0:
			number = number/2
		else:
			number = number * 3 + 1
	print(number)
	print('it took ' + str(count) + ' steps to go to 1 from ' + str(saved_number) +'!')

hailstorm(1.0)
