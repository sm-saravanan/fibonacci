
cache = {}
def fib(n, cache):
    if( n ==1 or n ==2):
        return 1
    else:
        if( cache.get(n, None) != None ):
            return cache[n]
        else:
            cache[n] = fib(n-1, cache) + fib(n-2,cache)
            return cache[n];
n = int(input('Enter n number: '))

print(f'fib({n}) is {fib(n, cache)} ')

        
