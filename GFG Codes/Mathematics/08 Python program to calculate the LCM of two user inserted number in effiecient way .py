##Python program to calculate the LCM of user inputted number in effiecient Euclidean Method
def gcd(a,b):
    if  b == 0:
        return a
    return gcd(b, a%b)
    
def lcm(a,b):
    
    return a*b //gcd(a,b)
    
    
if __name__ == '__main__':
    a = int(input("enter the alue of num1 " ))
    b = int(input("Enter the val;ue of num2 "))
    print(lcm(a,b))