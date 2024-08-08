#Python program to find the user inserted key element in the array 


def LinearSearch(arr, key):
    
    for i in range(len(arr)):
        if arr[i] == key:
            return key
            
    return -1

key =int(input("Enter the Value of Key element "))
arr = [10,20,32,34,45,56,76,89,76,44,33,11]

if(LinearSearch(arr, key) == -1):
    print("Element is not found ")
else:
    print("The user inputted element",key,"is present in array ")



