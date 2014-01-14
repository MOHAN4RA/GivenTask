def search(sorted_list, n):
    try:
	if n in sorted_list:
	  print "Its in index position:%r"% sorted_list.index(n)
    except IndexError:
	  print "ERROR: -1"
	
def split(all):
	# "This function separated the input with single quotes"
	bounce = all.split(' ')
	return bounce

def sorted_list(nos):
	"""Sorting the number"""
	return sorted(nos)


print "Enter the numbers separated by space between them:"
number = raw_input()

ball = split(number)
print "you entered: %r" % ball

sort = sorted_list(ball)
print "The sorting list is:"
print sort

print "Entered the number you want to search:"
find = raw_input()
search(sort, find)
