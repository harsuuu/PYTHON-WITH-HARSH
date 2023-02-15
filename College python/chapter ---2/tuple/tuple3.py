#Update Tuple
#we can not change tuple but there is a workaroud. We can convert the tuple into a list , change the list into the tupple.


x=('apple','bnana','cherry')
y=list(x)
y[1]='kiwi'
x=tuple(y)
print(x)