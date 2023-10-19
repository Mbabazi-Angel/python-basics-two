#write a python program that takes in a student name, the class and the section
student_name = "MBABAZI ANGEL"
print(type(student_name))
print(str(student_name))
the_class = "first year"
print(type(the_class))
print(str(the_class))
the_section = "semester one"
print(type(the_section))
print(str(the_section))

#write a program that takes in the student's five marks, total and percentage of the marks
programming = 75
mathematics = 60
communication_skills = 80
data_science = 70
computer = 85
Total_mark = (programming + mathematics + communication_skills + data_science + computer)
print(type(Total_mark))
print(str(Total_mark))
Percentage_of_the_mark = Total_mark/100
print(type(Percentage_of_the_mark))
print(str(Percentage_of_the_mark))


#To make an interactive program of the above question


programming_mark = float(input("Enter programming_mark:"))
print(programming_mark)
mathematics_mark = float(input("Enter mathematics_mark:"))
print(mathematics_mark)
communication_skills_mark = float(input("Enter communication_skills_mark:"))
print(communication_skills_mark)
data_science_mark = float(input("Enter your data_science_mark:"))
print(data_science_mark)
computer_mark = float(input("Enter your computer_mark:"))
print(computer_mark)
Total_mark = (programming_mark + mathematics_mark + communication_skills_mark + data_science + computer_mark)
print(type(Total_mark))
print("The total mark is" + " " + str(Total_mark))
Percentage_of_the_mark = Total_mark/5
print(type(Percentage_of_the_mark))
print("The percentage mark is" + " " + str(Percentage_of_the_mark))
print(f"Dear {student_name} and you are in {the_class} and in {the_section}, your percentage mark is {Percentage_of_the_mark}//%")