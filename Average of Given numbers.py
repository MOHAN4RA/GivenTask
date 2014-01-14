def split(numbers):
	all = numbers.split(' ')
	return all


print "Enter the numbers you want to sum separated by space between them:"
num = raw_input()
tot = split(num)
print tot
all = sum(int(i) for i in tot)
print all