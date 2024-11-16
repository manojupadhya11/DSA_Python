#03 Python Program to check whether user inserted number is a Palindrome numberor not

def pali(n):
    rev = 0
    
    temp = n
    
    while temp != 0:
        ld = temp %10 
        
        rev = rev *10+ld
        
        temp = temp // 10
    
    
    return rev
    
    
if __name__ =="__main__":
    
    num = int(input("Enter the number to check whether it is palindrome or not "))
    
    x = pali(num)
    
    if x == num:
        print(num,"is a Palindrome Number")
    else:
        print(num, "is not a Palindrome")