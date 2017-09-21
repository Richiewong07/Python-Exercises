# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
# n = 600851475143

# create an array of known_primes
known_primes = [2,3]
def is_prime(n):
	total_primes = len(known_primes)
	for i in range(0,total_primes):
		if(n % known_primes[i] == 0):
			# NOT PRIME!!
			return False
		else:
			# it might be prime, it might not.
			# Its just not divisible by this number
			continue
	known_primes.append(n)
	return True

print is_prime(4534532235)
