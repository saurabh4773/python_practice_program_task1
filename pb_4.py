while True:
    print("Menu")
    print("1. Check whether number is prime \n2. Find factorial of number \n3. Check whether number is palindrome \n4. Check whether number is Armstrong \n5. Exit")
    choice=int(input("Enter your choice : "))

    if choice==1:
        a = int(input("Enter the number : "))
        if a > 1:
            for i in range(2,int(a/2)+1):
                if(a % i) == 0:
                    print(a,"is not a prime number")
                    break
            else:
                print(a,"is a prime number")
        else:
            print(a,"is not a prime number")
    
    
    elif choice==2:
        a = int(input("Enter the number : "))
        factorial = 1
        if(a < 1):
            print("sorry, factorial does not exist for negative number")
        elif(a == 0):
            print("Factorial of zero is 1")
        else:
            for i in range(1,a + 1):
                factorial = factorial*i
            print("The factorial of",a,"is",factorial)

    
    elif choice==3:
        a = int(input("Enter the number : "))
        b = str(a)
        c = str(a)[::-1]
        if(b == c):
            print(a,"is palindrome")
        else:
            print(a,"is not palindrome")

    
    elif choice==4:
        a = int(input("Enter the number : "))
        b = list(map(int,str(a)))
        c = list(map(lambda x:x**3,b))
        d = sum(c)
        if(a == d):
            print(a,"is a Armstrong number")
        else:
            print(a,"is not a Armstrong number")
    
    
    elif choice==5:
        break
    
    
    else:
        print("Invalid choice")