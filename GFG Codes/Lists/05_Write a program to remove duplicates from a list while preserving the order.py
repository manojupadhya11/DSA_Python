#5.	Remove Duplicates
#	Write a program to remove duplicates from a list while preserving the order.


mylist = [2,3,4,5,6,7,8,12,12,14,11,15,16,17,18,2,3,4,6]


unique_list = []


def list_duplicate_check(mylist,unique_list):
    for x in mylist:
        if x not in unique_list:
            unique_list.append(x)
    print(unique_list)

list_duplicate_check(mylist,unique_list)