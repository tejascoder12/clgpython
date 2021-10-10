def word(str):
    j=len(str)-1
    for i in range(int(len(str)/2)):
        if str[i]!=str[j]:
            return False
        j=j-1
    return True
    
str=input("Enter the string :")
ans=word(str)

if(ans):
    print("string is palindrome")
else:
    print("string is not palindrome")