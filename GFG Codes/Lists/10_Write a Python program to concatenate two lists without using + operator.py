#10 10.	Concatenate Two Lists
#	Write a program to concatenate two lists without using the + operator.

list1 = [10,20,30,40,50]

list2 = [11,22,33,44,55]


#first approach
#list1.extend(list2)
#print(list1)

#second approach


for item in list2:
    list1.append(item)

print(list1)