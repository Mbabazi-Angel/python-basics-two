student_marks = [60,70,80]
#data type of students_name
#print type students marks
print(student_marks)
#list accessing
#positive indexing
print(student_marks[1])
#negative indexing
print(student_marks[-1])
#list slicing
print(student_marks[1:2])
print(student_marks[1:3])
#checking if item exists
if 80 in student_marks:
    print("yes, 80 is in student_marks")
else:
    print("no, 80 is not in student_marks")
if 100 in student_marks:
    print("yes, 100 is in student_marks")
else:
    print("no, 100 is not in student_marks")    