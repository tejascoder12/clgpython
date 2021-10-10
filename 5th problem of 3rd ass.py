str1=input("Enter the string :")
list1=str1.split()
list2=set(list1)
list3=list(list2)

print(list1)
print(list2)
print(list3)

list4=[]
list5=[]
counter=0

for i in range(len(list3)):
	counter=0
	for j in range(len(list1)):
		if list3[i]==list1[j]:
			counter+=1
	list4=list3[i],counter
	list5.append(list4)
print(list5)
	