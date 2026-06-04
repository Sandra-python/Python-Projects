students=[]
while True:
	name=input("Enter the name: ")
	m=int(input("Enter the maths mark: "))
	p=int(input("Enter the physics mark: "))
	c=int(input("Enter the chemistry mark: "))
	Total= m+p+c
	Average = Total/3
	students.append([name,m,p,c,Total,Average])
	d=input("Do you wish to continue(Y/N): ")
	if d.lower()=='y':
		continue
	else:
		break

print("Name  Maths   Physics   Chemistry")
for i in students:
	print(i[0],  i[1],   i[2],   i[3])
	print("Total: ",i[4],"Average: ",i[5])
    