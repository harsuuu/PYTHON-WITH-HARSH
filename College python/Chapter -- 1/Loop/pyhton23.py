num=int(input("Enter the numbetr"))
sum=0
while(num>0):
    rem=num%10
    num=num/10
    sum=sum+rem*rem*rem
    