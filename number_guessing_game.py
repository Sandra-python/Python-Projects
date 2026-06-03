import random
number=random.randint(1,20)
print("Guess a number between 1 and 20.")
print("You have maximum 5 guesses. Lets START.")

i=0
while True:
	guess=int(input("\nEnter your guess: "))
	if guess>number:
		print("Too High")
	elif guess<number:
		print("Too Low")
	else:
		print("Correct! You won!")
		break
	i=i+1
	print(5-i,"guesses remaining")
	
	if i==5:
		print("The correct number was ",number)
		break
print("GAME OVER!")