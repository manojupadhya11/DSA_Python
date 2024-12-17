#2. Find the Largest Element in a List
#	Write a program to find the largest number in a list.

mylist = [10,40,3,4,5,6,56,19,20,21,45]
largest = 0
second_largest = 0
for i in range(len(mylist)):
    if mylist[i] >= largest :
        largest = mylist[i]
    elif mylist[i] >= second_largest :
        second_largest = mylist[i]
print("second_largest number in the given list is ",second_largest)
