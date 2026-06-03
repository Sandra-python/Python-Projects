print("Welcome to Quiz")
print()
score=0
print("Q1. Capital of India?")
a=["Delhi","Mumbai","Goa"]
for i in range(len(a)):
	print(i+1,".",a[i])
ans=input("Enter your answer: ")
if ans.lower()=="delhi":
	print("Correct!")	
	score=score+1
else:
	print("Wrong.")
print("\n Q2.Which is the national animal of India?")
b=["Lion","Tiger","Leopard"]
for i in range(len(b)):
	print(i+1,".",b[i])
ans=input("Enter your answer: ")
if ans.lower()=="tiger":
	print("Correct!")
	score=score+1
else:
	print("Wrong.")
print("\n Q3. 2+2= ?")
c=[4,6,8,2]
for i in range(len(c)):
	print(i+1,".",c[i])
ans=input("Enter your answer: ")
if ans=="4" or ans.lower()=="four":
	print("Correct!")
	score=score+1
else:
	print("Wrong.")
print("Score:",score)
if score==3:
	print("Excellent")
elif score==2:
	print("Very Good")
else:
	print("Try again")