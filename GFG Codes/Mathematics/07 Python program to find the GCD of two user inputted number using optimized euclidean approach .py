#03 Python Program to find the the greatst common divisor of two numbers using euclidean algorithm
def GCD(num1, num2):
    if num2 == 0:
        return num1
    return GCD(num2, num1%num2)
    
if __name__ == "__main__":
    
    num1 = int(input("Enter the number1 "))
    num2 = int(input("Enter the number2 "))
    
    print(GCD(num1, num2))