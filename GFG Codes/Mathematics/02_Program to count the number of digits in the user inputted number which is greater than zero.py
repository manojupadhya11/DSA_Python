#02 Count number of digits in the number when user inputted number is greater than zero

n = int(input("Enter the value of n "))
digit = 0
temp = n
while n != 0:
    n = n//10
    digit = digit+1
    
    


print("The total number of digits in ",temp,"is : - ",digit)