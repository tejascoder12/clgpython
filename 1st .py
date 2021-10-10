groupA=["Aman ","Raj ","Atharav","ruchi"]
groupB=["Aman","Saloni","Aditya","Ayush","Atharav"]
groupC=["Raj","Ruchi","Vedant","Atharav"]

resultCB=[ ]
for i in groupA:
	for j in groupB:
		if (i==j):
			resultCB.append(j);
			break;
print("List of student playing crickrt and badminton is :",resultCB)