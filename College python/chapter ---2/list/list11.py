num=[]
n=int(input("Enter the Number : "))
for i in range(n):
    value=int(input("Enter the Value: "))
    num.append(value)
    
    
for i in num:
    if(i%2==0):
    even.append(i)
    
print(num)
print(even)