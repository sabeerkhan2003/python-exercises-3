def palin(n):
    temp=n
    pal=0
    while temp>0:
        rem=temp%10
        pal=pal*10+rem
        temp//=10
    if pal==n:
        print("palindrome")
    else:
        print("not palindrome")
palin(1551)        
