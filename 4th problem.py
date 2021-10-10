groupA=["Aman","Raj","Atharva","Ruchi"]
groupB=["Aman","Saloni","Aditya","Ayush","Atharva"]
groupC=["Raj","Ruchi","Vedant","Atharva"]

lena=len(groupA)
lenb=len(groupB)
lenc=len(groupC)

print("Number of students who play cricket and football but not badminton: ")

result1=[];


for i in range(lenc):
  for j in range(lena):
    if(groupC[i]==groupA[j]):
      result1.append(groupC[i]);
      break;

resultlist=[];
len1=len(result1)
flag=0;
for i in range(len1):
	for j in range(lenb):
		if(result1[i]==groupB[j]):
			flag=1;
	if(flag==0):
		resultlist.append(result1[i]);
print(len(resultlist))
print(resultlist)