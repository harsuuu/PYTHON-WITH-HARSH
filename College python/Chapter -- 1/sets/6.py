setA={1,2,3}
print(setA)   #Befor adding the element
setA.add(4)   
print(setA)  #after adding

setA.remove(4)
print(setA)

print(setA.clear())         #clear()


a={1,2,3,4,5,6,7}
b={1,2,3}
print(a.issubset(b))      #ye btayega ki bo a subset h ki nhi b ka.

print(a.issuperset(b))    #means b ke sare element a m hai.