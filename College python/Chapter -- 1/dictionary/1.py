from turtle import st


student={
    'Name': ['Harsh'],
    'branch': ['CST SPL'],
    'Age':['20'],
    'Behaviour':['Good']
}
print(student)
print(student['Name'])
print(student['Age'])



#get()
print(student.get('branch'))

#get keys()
print(student.keys())

#get Values()
print(student.values())

#if i want to change the Name, Harsh --> Harshu

student['Name']="Harshu"
print(student)

#second method 
student.update({'Name':'Harshuu'})
print(student)

#adding the elements
student['Sex']='Male'
print(student)


#REmoving the elements
student.pop('branch')    #1st method
print(student)

del student['Sex']       #2nd method
print(student)    

print(student.clear())   #3rd Method