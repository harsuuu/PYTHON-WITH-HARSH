#if--elif--else
#largest among three number
num1=int(input("Enter the number1:"))
num2=int(input("Enter the Number2:"))
num3=int(input("Enter the Number3:"))
max=num1
if(max<num2):
    max=num2
elif(max<num3):
    max=num3

print(max)

