def palindrome(str1):
    str2 = str1[::-1]
    if(str1 == str2):
        print(str1,"is a palindrome")
    else:
        print(str1,"is not a palindrome")

str1 = str(input("Enter the string : "))
palindrome(str1)