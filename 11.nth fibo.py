def nth_fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 1
    else:
        return nth_fibo(n-1)+nth_fibo(n-2)
print(nth_fibo(8))
