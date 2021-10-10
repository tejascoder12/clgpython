groupA=["Aman","Raj","Atharva","Ruchi"]
groupB=["Aman","Saloni","Aditya","Ayush","Atharva"]
groupC=["Raj","Ruchi","Vedant","Atharva"]

lena=len(groupA)
lenb=len(groupB)
lenc=len(groupC)

print("Number of students who play neither cricket nor badminton:")

result=[];


for i in range(lenc):
  for j in range(lena):
    if(groupC[i]==groupA[j]):
      flag=1;
      break;
  for k in range(lenb):
    if(groupC[i]==groupB[k]):
        flag=1;
        break;
  if(flag==0):
    result.append(groupC[i]);
  flag=0;

print(result)