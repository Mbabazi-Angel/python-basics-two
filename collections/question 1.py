#Consider a list a = [1,1,2,3,5,8,13,21,34,55,89]. Write a program that prints out all the elements of the list that are less than 5
a = [1,1,2,3,5,8,13,21,34,55,89]
#new_list with items less than 5
#for conditional statements e.g <5, use if
for items in a:
    if items < 5:
        print(items) 

#Another approach
a = [1,1,2,3,5,8,13,21,34,55,89]
#create a new list with elements less than 5
#first create an empty list 
new_list = []
for items in a:
    if items < 5:
        new_list.append(items) #append means to add/insert items
        new_list.sort()
        print(new_list)