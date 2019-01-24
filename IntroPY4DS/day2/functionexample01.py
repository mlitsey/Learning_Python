def isprime(n):      # define the isprime function allow n to be a param passed in
    if n<= 1:        # is param passed in is 1 return false... not a prime number
        return False 
    for x in range(2,n):  # start iterating through the numbers starting a 2 until n
       if n % x == 0:    # if no remainder, then say it's not a prime
           return False  # not a prime, means return false
       else:             # is a prime
           return True   # return true
        
def list_primes():
    for n in range(100):
       if isprime(n):
          print(n, end=",",flush=True)
    print()
    
list_primes()