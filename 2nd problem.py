groupA=["Aman","Raj","Atharva","Ruchi"]
groupB=["Aman","Saloni","Aditya","Ayush","Atharva"]
groupC=["Raj","Ruchi","Vedant","Atharva"]

lena=len(groupA)
lenb=len(groupB)

print("List of students who either play cricket or badmintion but not both")

resultCBN=[];
flag=0;
for i in range(lena):
  for j in range(lenb):
    if(groupA[i]==groupB[j]):
      flag=1;
  if (flag==0):
    resultCBN.append(groupA[i])
  flag=0;


for i in range(lenb):
  for j in range(lena):

    if(groupB[i]==groupA[j]):
      flag=1;
  if (flag==0):
    resultCBN.append(groupB[i]);
  flag=0;

print(resultCBN)