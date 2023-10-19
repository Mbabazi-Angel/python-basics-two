#Write a python function to find the maximum of three numbers.
#a=70, b=80, c=65
def maximum_value(a,b,c):
    if a>b and a>c: #if one of the statements is false then the whole statement is false hence false
        print(f'{a} is greater than {b} and {c}')
    elif b>a and b>c: #else if
        print(f'{b} is greater than {a} and {c}')
    else:
        print(f'{c} is greater than {a} and {b}')
maximum_value(70,80,65)        

#Write a python program to sum all numbers in the list
#m = [8,2,3,0,7]
def sum_of_numbers(list):
    for x in list: 
     print (x)
     output = (list)
list = [8,2,3,0,7]
sum_of_numbers(list)
print(f'The sum of {list} is {}')     
