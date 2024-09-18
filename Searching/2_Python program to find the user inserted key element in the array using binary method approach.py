#Python program to find the user inserted key element in the array using binary method approach

# Returns index of x in arr if present, else -1
def BinarySearch(arr, low, high, key):
 	# Check base case   
    if high>=low:
        mid = (high + low )//2
        
        if arr[mid] == key:
            return mid
        
		# If element is smaller than mid, then it can only
		# be present in left subarray
        elif arr[mid] > key:
            return BinarySearch(arr, low, mid-1, key)
        
        else:
            return BinarySearch(arr, mid+1, high, key)
    
    else:
        return -1


arr = [10,20,30,40,50,60,70,80,90]

key =int(input("Enter the Value of Key element "))

result = BinarySearch(arr, 0, len(arr)-1, key)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

