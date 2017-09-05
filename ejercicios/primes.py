# 1)
def is_prime (n):
	for i in range(2, n):
		if n % i == 0:
			return False
	return True

# 2)
for i in range(0, 1000):
	print str(i) + ' heuhuehuehue ' + str(is_prime(i))

# 3)
print [is_prime(x) for x in range(1, 100)]