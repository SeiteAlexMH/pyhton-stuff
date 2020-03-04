def next_happy_year(year):
	n = 0
	year_found = True
	while n <10.0:
		m = str(year).count(str(n))
		if m <= 1:
			pass
		else:
			year_found = False
		n+=1
	return year_found

if next_happy_year(2013):
	 print('success')
else:
	print('fail')
