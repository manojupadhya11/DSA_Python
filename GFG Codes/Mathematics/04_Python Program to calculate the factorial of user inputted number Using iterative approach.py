#03 Python Program to find the factorial of user inserted number 
def factorial(n):
    res = 1
    for i in range(2, n+1):
        res = res*i
    return res
    
if __name__ == "__main__":
    
    num = int(input("Enter the number to calculate the factorial of number "))
    
    print(factorial(num))
