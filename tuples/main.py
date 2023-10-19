#difference between lsts, sets and tuples
#list = [1,2,3,4,5,6]
#tuple = (1,2,3,4,5,6)
#sets = {1,2,3,4,5,6}

#Lists are mutable/changeable, an duplicate
#Tuples are immutable, ordered and allow duplicates
#Sets are immutable,dont allow duplicate values and count them as one 



#TUPLES
marks = (80,79,69,70)
marks[0]
print(type(marks))

#Access items in a tuple (acccess the 1st item)
print(marks[1])
print(len(marks))

#integer
mark = 80
print(mark)
print(type(mark))

#tuple
mark = (80,)
print(mark)
print(type(mark))


#Check whether 79 exists in the variable marks and if it does, print 79 is a member of variable marks
#Check whether 88 belongs to variable marks and if it does not, print that the value is not an item of the variable

marks = (80,79,69,70)
#Instead of two different if else statements for 79 and 88 just merge the two since else statements coves the rest
if 79 in marks:
    print('79 is a member of the variable marks')
else:
    print('88 is not a member of the variable marks')

#String interpolation (use to create statements without concutinating(+) hence use the formater(f))
name = 'Mbabazi Angel'
age = '19 years old'
print(f"I'm {name} and I'm {age}")

#Modifications of the tuples
#Change 79 to 88
marks = (80,79,69,70)
#change the tuple to a list in order to modify
new_marks = list(marks)
print(type(new_marks),new_marks)
new_marks[1] = 88
#change back to a tuple
updated_marks = tuple(new_marks)
print(new_marks)
print(tuple(new_marks))

#Add 99 to the tuple 
updated_marks = list(new_marks)
print(updated_marks)
updated_marks.append(99)
print(updated_marks)
print(tuple(updated_marks))