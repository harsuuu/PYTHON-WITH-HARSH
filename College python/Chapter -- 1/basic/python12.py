unit=int(input("Enter the unit"))
if(unit>200):
    bill1=(unit-200)*10
    unit=200
if(unit<=200):
    bill2=(unit-100)*5
    unit=100
if(unit<=100):
    bill3=0

bill=bill1+bill2+bill3
print(bill)