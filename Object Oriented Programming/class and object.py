#Create a class. 
#it is always in singular adnd starts with a capital letter i.e Student
#list properties that connect to the Student class e.g student no, name, email, contact, age, cohort
#create methods 

class Student:
    #student_no  
    #name  
    #email 
    #contact  
    #age 
    #cohort
    def __init__(self,student_no,name,email,contact,age,cohort):
        self.student_no = student_no
        self.name = name
        self.email = email
        self.contact = contact
        self.age = age
        self.cohort = cohort 

#String representation of an object
    def __str__(self):
        return f'{self.student_no}, {self.name},{self.age}, {self.cohort},{self.email},{self.contact}'
    

#Create an object (instance)
#each has the same attributes from the class 
student1 = Student('2023/DCSE/0040/SS', 'MBABAZI ANGEL', 'mercy04angel@gmail.com', '0770935269', 19, 'cohort three')
print(student1)


#Create a function that returns the student's name, their cohort and the email adress. 
#Access this function using any instance of the class

class User:
    def __init__(self,name,cohort,email):
        self.name = name
        self.email = email
        self.cohort = cohort 
    def __str__(self):
        return (f'{self.name},{self.cohort},{self.email}')
User1 = User('MBABAZI ANGEL','COHORT THREE', 'mercy04angel@gmail.com')
print(User1)    
    

