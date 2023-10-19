#We use the def syntax (define functions) in python
#the def keyword means define

def mycourse():
    print('Programming in python')

#Function with parameters 
def myname():
    print('Mbabazi Angel')
#calling the function so that it performs the particular task
myname()
mycourse()

#Create a function that multiplies two numbers a and b where a is 3 and bis 10
def product_of_two_numbers(a,b):
    output = a*b
    print(f'The product of {a} and {b} is {output}')
product_of_two_numbers(3,10) #calling the function

#Create a function that returns your name and your age as argument of the function
def my_name_and_age(name, age):
    print(f'My name is {name} and I am {age}')
my_name_and_age('Angel', 19)



