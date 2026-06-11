n=input("Enter the name to search: ")
p=open("abc.txt","r")
while True:
	X=p.readline()
	if X=='':
		break
	y=X.split("-")
	if n.lower()==y[0].lower():
		print(X)
p.close()
	