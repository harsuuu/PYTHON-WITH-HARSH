mydict = {
    "Fast" : "As soon as possible",
    "Harsh" : "A simple boy",
    "marks" : [1,2,3] ,
    "another" : {'harsh' : 'a good boy'},
    1 : 2
}

print(mydict.get("Harsh"))    
print(mydict['Harsh'])            
 
# now we see what is difference let assume we print this 

print(mydict['harsh2'])    #harsh2 nhi hai dictionary to ye "error" dega

print(mydict.get("harsh2"))   # get se ye error nhi dega ye "none" return krenga "interview question"