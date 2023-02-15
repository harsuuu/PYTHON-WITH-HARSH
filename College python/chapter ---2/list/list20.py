#Consider the list with mixed type of element , such as L1=[1,'a',3.45,'b',8,2.5]. Create another list using list comprehension which consists of only the integer elements presents within the list.

l1=[1,2.5,'z',3,'a',5.67]
l1=[x for x in l1 if(type(x)== int)]