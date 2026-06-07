p=open("abc.txt","a")
while True:
	name=input("Enter the name: ")
	phone=input("Enter the phone no: ")
	p.write(name+"-"+phone+"\n")
	ch=input("Do you want to continue(Y/N): ")
	if ch.lower()=='y': 
		continue
	else:
		break
p.close()