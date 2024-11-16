#03 Python Program to find the factorial of user inserted number 
def factorial(n):
    if n == 0:
        return 1
    else: 
        return n*factorial(n-1)
    
if __name__ == "__main__":
    
    num = int(input("Enter the number to calculate the factorial of number "))
    
    print(factorial(num))
