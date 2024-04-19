#6->1,2,3
#8->1,2,4

#WAP to check whether the given number is perfect or not



n=int(input("enter a number:"))
sum=0
i=1
while i<n:
    if n%i==0:
        
        sum+=i
    i+=1
if sum==n:
    print("perfect")
else:
    print("not perfect")

    