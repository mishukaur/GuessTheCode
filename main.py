import random
Code = []
Guesses = ["_", "_", "_", "_"]
Letters = ["A", "B", "C", "D", "E", "F"]
for x in range(4):
	Code.append(random.choice(Letters))

userinput = list(input("Guess the code!: "))

while Code != userinput:
	for x in range(len(userinput)):
		if userinput[x] == Code[x]:
			Guesses[x] = 1
		elif userinput[x] in Code and userinput[x] != Code[x]:
			Guesses[x] = 2
		elif userinput[x] not in Code:
			Guesses[x] = 3
	print(Guesses)

	if Code == userinput is True:
		print("You guessed the code!")
		break

	userinput = list(input("Guess the code!: "))
