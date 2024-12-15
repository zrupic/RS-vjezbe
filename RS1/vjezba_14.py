#zadatak 1
def isPrime(broj):
    if broj <= 1:
        return False
    for i in range (2, broj):
        if broj % i== 0:
            return False
    return True
    
print(isPrime(7))
print(isPrime(-1))
print(isPrime(10))
print(isPrime(11))
print(isPrime(22))

#zadatak 2
def is_Prime(broj):
    if broj <= 1:
        return False
    for i in range (2, broj):
        if broj % i== 0:
            return False
    return True
def primes_in_range(start, end):
    return [broj for broj in range(start, end + 1) if is_Prime(broj)]
print(primes_in_range(1, 10))