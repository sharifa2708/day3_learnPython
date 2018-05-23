def fib2(n):
    a,b =0,1
    result = []
    while b<n:
        result.append(b)
        a,b= b, a+b
    return result

x= fib2(100)
print(x)

print(fib2(100))
print(fib2(0))

