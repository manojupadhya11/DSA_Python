#2. Find the Largest Element in a List
#	Write a program to find the largest number in a list.

mylist = [10,40,3,4,5,6,56,19,20,21,45]
maxelement = 0 
for i in range(len(mylist)):
    if mylist[i] > maxelement :
        maxelement = mylist[i]
        
    
print("Largest number in the given list is ",maxelement)
