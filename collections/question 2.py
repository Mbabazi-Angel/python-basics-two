#Consider two lists a = [1,1,2,3,5,8,13,21,34,55,89], b = [1,1,2,3,4,5,6,7,8,9,10,11,12,13] 
#Write a program that returns a list that contains only the elements that are common between the lists without any duplicate item in the new list
a = [1,1,2,3,5,8,13,21,34,55,89]
b = [1,1,2,3,4,5,6,7,8,9,10,11,12,13]

length = len(a)
print(length)

length = len(b)
print(length)

common_list = []
for x in a:
    for y in b:
        if y in common_list:
            continue
        else:
            common_list.append(y)
common_list = set(a) & set(b)
print(common_list)

print(len(a))
print(len(b))