#4.	Check if a List is Sorted
#	Write a function to check whether a list is sorted in ascending order.


mylist = [2,3,4,5,6,7,8,12,14,11,15]


#mylist = [2,3,4,5,6,7,8,12,14,15]


def list_sort_check(mylist):
    for i in range(len(mylist)-1):
        if mylist[i] > mylist[i+1]:
            return False
    return True

    
if list_sort_check(mylist) == True:
    print("The list is sorted using ascending order")
else:
    print("The list is not sorted using ascending order")
    
