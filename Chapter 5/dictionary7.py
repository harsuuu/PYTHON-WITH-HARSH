mydict = {
    "Fast" : "As soon as possible",
    "Harsh" : "A simple boy",
    "marks" : [1,2,3] ,
    "another" : {'harsh' : 'a good boy'},
    1 : 2
}

print(mydict)                 # isme sirf uper bala print hoga
updatedict = {                # yha hum update kr skte haii apni uper bali dictionary k aage
    "name" : "harsh",
    "marks" : [45,56]
}                               
mydict.update(updatedict)      
print(mydict)        