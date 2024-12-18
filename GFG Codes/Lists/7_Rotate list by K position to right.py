#7.	Rotate a List
#	Rotate a list by k positions to the right (e.g., [1, 2, 3, 4, 5] rotated by 2 becomes [4, 5, 1, 2, 3]).


mylist = [1,2,3,4,5]
k = int(input("enter the number to position to rotate "))

len_list = len(mylist) - k
output_list = []

for i in range(len_list, len(mylist)):
    output_list.append(mylist[i])

for i in range(0, len_list):
    output_list.append(mylist[i])
    
    
print(output_list)