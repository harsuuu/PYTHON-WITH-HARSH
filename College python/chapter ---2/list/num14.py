num=[1,2,1,2,3,4,2,2,2]
print(num.count(1))
print(num.count(2))


#Copy element
list1=['z','y','a']
list2=list1.copy()
print(list2)


#Extend
list1=['a','b','c']
list2=[1,2,4]
list1.extend(list2)
print(list1)


#index
alpha=['a','b','c','d']
print(alpha.index('d'))


#insert  --->means index number pr koi number add krna.
num=[5,10,28]
num.insert(2,15)
print(num)

#reverse 
beta=['a','b','c']
beta.reverse()
print(beta)

#length

num=[11,22,33,44,55]
print(len(num))


#max
num=[11,22,33,44,55]
print(max(num))


#sum

num=[1,2,3,4,5,6]
print(sum(num))

#min

num=[11,4,3,2]
print(min(num))
