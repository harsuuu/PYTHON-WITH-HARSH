#count even and odd number in number

num=int(input("Enter the number"))
odd_count=0
even_count=0
while (num>0):
    rem=num%10
    if(rem%2==0):
        even_count=even_count+1
    else:
        odd_count=odd_count+1

    num=num//10
print(even_count)
print(odd_count)