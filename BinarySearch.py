array = [1,2,3,4,5,6,7,8,9,10]
min = 0;
max = len(array)-1
maxint = 10

for i in range(len(array)):
	if array[i] > 8:
		for index in range(len(array)):
			if max < min:
				print "not in list"
				break
			guess = (max+min)/2
			if array[guess] == 8:
				print "found it!"
				break
			elif array[guess] < 8:
				min = guess+1
				print "guess too low, keep looking"
			else: 
				max = guess-1
				print "guess too high, keep looking"
		print maxint



