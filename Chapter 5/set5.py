a = set()
a.add(5)
a.add(7)
#  a.add([1,2,3])     #set k ander list ko add nhi kr skte hai qki  mutable hai
a.add((1,2,4))        #set k ander tupple ko add kr skte hai qki tupple unmutable hai
#a.add({2:3})          #set k ander dictionary bhi add nhi kr skte qki ye bhi mutable hai
print(a)
  