str=input("Enter the string:")
sub=input("Enter the sub string:")
j=0


for i in range(len(str)):
    if(str[i]==sub[j]):
        j=j+1
        if j==len(sub):
          index=i-(len(sub)-1)
          break;
    else:
        j=0
print(index)