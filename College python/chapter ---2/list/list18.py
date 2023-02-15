#write a program to create the list with elements 1,2,3,4 and 5. Display even element of list using list comprehensive.


num=[1,2,3,4,5]
num=[(x for x in num if(x%2==0))]
print(num)
