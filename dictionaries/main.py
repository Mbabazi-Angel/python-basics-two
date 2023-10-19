#keys (name = Angel, age = 19, address = Kasubi, cohort = 3)
student = {
    'name': 'Angel',
    'age': 19,
    'address': 'Kasubi',
    'cohort': 'three'
}
print(type(student))

#Access the dictionary items
#Either
print(student['name'])
#Or
#get()
print(student.get('name'))
print(student.keys())