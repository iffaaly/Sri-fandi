def is_prime(n):
 if n < :
 return False
 for i in range(, int(n ** .) + ):
 if n % i == :
 return False
 return True
print(is_prime())