import math

def isPrime(n: int) -> bool:
    if n <= 1:
        return False
    count: int = 2
    while(count <= int(math.sqrt(n))):
        if n % count == 0:
            return False
        count += 1
    return True

def printResult(n) -> None:
    if isPrime(n):
        print('{} is a Prime'.format(n))
    else:
        print('{} is not a Prime'.format(n))

n = int(input('Please a number: '))

printResult(n)

        
    
