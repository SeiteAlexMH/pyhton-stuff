#Fizz Buzz
#Alexandre Seite

def FizzBuzz():
	Dividers = [3,5]
	Output = ['Fizz','Buzz']
	index = 1
	while index < 101:
		n = 0
		returnString = ''
		while n < len(Dividers):
			if index % Dividers[n] == 0:
				returnString += Output[n]
			n += 1
		print(str(index) + ' ' + returnString)
		index += 1

FizzBuzz()
