def deposit(amt):
	global balance
	balance=balance+amt
	
def withdrawl(amt):
	global balance
	if(balance>amt):
		balance=balance-amt
		
tranlog=[ ]
balance=0

while True:
	data=input("please enter transation details: ")
	if (data=='Exit' or data=='exit'):
		break;
	tranlog.append(data.split())
print(tranlog)

for var in tranlog:
	if(var[0]=='D' or var[0]=='d'):
		deposit(int(var[1]))
	elif(var[0]=='W' or var[0]=='w'):
		withdrawl(int(var[1]))
print("Balance is :",balance)