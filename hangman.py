#Michelle Holden
#Simple Hangman Game
# 10/16/2018

username= input("What is your name? ")

print("Hello " + username, "Let's play hangman!")
#print("Please guess one letter.")




word= "destiny"

numGuess= ''
turns= 10

while turns > 0:
	incorrect= 0
	
	for char in word:
		if char in numGuess:
			print (char)
		else:
			#print ("incorrect")
			incorrect+=1
	if incorrect== 0:
		print ("You won!")
		break

	guess= input("Please guess a letter ")
	numGuess+= guess
	if guess not in word:
		turns-=1
		print("Wrong")
		print("You have " + str(turns) + " more guesses")
		if turns== 0:
			print("You lost")

