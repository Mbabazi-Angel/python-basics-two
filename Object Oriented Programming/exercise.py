#create a class
class User_class:
  x = ('name', 'age', 'location')
print(User_class) 

#create a new instance of the User_class (a new object)
object = User_class()
print(object.x)

#Access the User's name & age
#We use the self parameter 

class User_class:
  def __init__(self, name, age,location):
    self.name = name
    self.age = age
    self.location = location 
  def __str__(self):
    return(f'Name:{self.name}, Age:{self.age}, Location:{self.location}')
User1 = User_class('MBABAZI ANGEL',19,'Kasubi')
print(User1)


  



