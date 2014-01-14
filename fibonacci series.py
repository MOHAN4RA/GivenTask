def fib(n):
	f1 = 0
	f2 = 1
	while f2 < n:
		f1 = f2
		f2 = f1 + f2
	print f2
	
print "How many Fibonacci"
all = raw_input()
fib(all)



