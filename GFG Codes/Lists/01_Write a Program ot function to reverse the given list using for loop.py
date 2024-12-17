#01_Write a Python Program to reverse a list without using reverse() function
#1.	Reverse a List
#	Write a function to reverse a given list without using the reverse () method.


mylist = ["Manoj","Manu","Greeshma","Sarada","Sandesh"]

#mylist.reverse()

#print(mylist[::-1])




# Create an empty list to store reversed elements
reversed_list = []


for i in range(len(mylist) - 1, -1,-1): 
    reversed_list.append(mylist[i])  
# Print the reversed list
print("Original List:", mylist)
print("Reversed List:", reversed_list)
