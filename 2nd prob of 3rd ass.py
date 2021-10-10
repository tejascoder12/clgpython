Str1=input("Enter the string: ")
Char=input("Enter the character: ")
cout=0

for i in range(len(Str1)):
  if Char==Str1[i]:
    cout=cout+1
print("Character ",Char,"present",cout,"times in given string")