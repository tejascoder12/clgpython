str1=input("Enter the string :")
list=str1.split()
maxlen=0
print(list)
for i in range(len(list)):
  if(maxlen<len(list[i])):
   maxlen=len(list[i])
print("The longest length is : ",maxlen)

for j in range(len(list)):
  if(len(list[j])==maxlen):
    print("The word with the longest length :", list[j])