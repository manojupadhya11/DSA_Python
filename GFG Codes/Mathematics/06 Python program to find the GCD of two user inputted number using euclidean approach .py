#03 Python Program to find the the greatst common divisor of two numbers using euclidean algorithm
def GCD(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
            
    return num1
if __name__ == "__main__":
    
    num1 = int(input("Enter the number1 "))
    num2 = int(input("Enter the number2 "))
    
    print(GCD(num1, num2))