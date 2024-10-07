import random
import time
import os

conArray = [
[" "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "]
]



def printBoard():
	os.system('cls')
	print("\n\n\n\n\n")
	for x in range(6):
		print("                                            _____________________________")
		print("                                            | ", end='')
		for y in range(7):
			print(conArray[x][y], " | ", sep='', end='')
		print("")
	print("                                            _____________________________")
	print("                                              1   2   3   4   5   6   7  ")
	print("\n\n")

def checkOpen(choice):
	for x in range(5, -1, -1):
		if conArray[x][choice] == " ":
			return x
	return -1

def intTest(textToDisplay):
	try:
		val = int(input(textToDisplay))
		return val
	except:
		printBoard()
		print("                                             Please enter a valid number")
		return -777333

def playerTurn():
	row = -1
	while row == -1:
		choice = intTest("                    Pick a number 1 - 7 to indicate which column you want to drop your token into: ")
		while choice < 1 or choice > 7:
			if choice != -777333:
				printBoard()
				print("                                          Your number is not within 1 and 7")
			choice = intTest("                    Pick a number 1 - 7 to indicate which column you want to drop your token into: ")
		choice = choice - 1
		row = checkOpen(choice)
		if row == -1:
			printBoard()
			print("                                                 This column is full!")
	conArray[row][choice] = "X"

def computerTurn():
	print("                                               Computer is thinking...")
	time.sleep(1)
	row = -1
	while row == -1:
		choice = random.randint(0, 6)
		row = checkOpen(choice)
	conArray[row][choice] = "O"

def checkVert():
	for y in range(7):
		for x in range(5, 2, -1):
			if conArray[x][y] == "X":
				if conArray[x - 1][y] == "X" and conArray[x - 2][y] == "X" and conArray[x - 3][y] == "X":
					return 0
			elif conArray[x][y] == "O":
				if conArray[x - 1][y] == "O" and conArray[x - 2][y] == "O" and conArray[x - 3][y] == "O":
					return 1
	return -1

def checkHor():
	for x in range(6):
		for y in range(4):
			if conArray[x][y] == "X":
				if conArray[x][y + 1] == "X" and conArray[x][y + 2] == "X" and conArray[x][y + 3] == "X":
					return 0
			elif conArray[x][y] == "O":
				if conArray[x][y + 1] == "O" and conArray[x][y + 2] == "O" and conArray[x][y + 3] == "O":
					return 1
	return -1

def checkUpRight():
	for x in range(5, 2, -1):
		for y in range(4):
			if conArray[x][y] == "X":
				if conArray[x - 1][y + 1] == "X" and conArray[x - 2][y + 2] == "X" and conArray[x - 3][y + 3] == "X":
					return 0
			elif conArray[x][y] == "O":
				if conArray[x - 1][y + 1] == "O" and conArray[x - 2][y + 2] == "O" and conArray[x - 3][y + 3] == "O":
					return 1
	return -1

def checkUpLeft():
	for x in range(5, 2, -1):
		for y in range(3, 7):
			if conArray[x][y] == "X":
				if conArray[x - 1][y - 1] == "X" and conArray[x - 2][y - 2] == "X" and conArray[x - 3][y - 3] == "X":
					return 0
			elif conArray[x][y] == "O":
				if conArray[x - 1][y - 1] == "O" and conArray[x - 2][y - 2] == "O" and conArray[x - 3][y - 3] == "O":
					return 1
	return -1

def checkDiag():
	winStatus = checkUpRight()
	if winStatus == 0 or winStatus == 1:
		return winStatus
	winStatus = checkUpLeft()
	if winStatus == 0 or winStatus == 1:
		return winStatus
	return -1

def checkTie():
	for x in range(6):
		for y in range(7):
			if conArray[x][y] == " ":
				return -1
	return 2


def checkWin():
	winStatus = checkVert()
	if winStatus == 0 or winStatus == 1:
		return winStatus
	winStatus = checkHor()
	if winStatus == 0 or winStatus == 1:
		return winStatus
	winStatus = checkDiag()
	if winStatus == 0 or winStatus == 1:
		return winStatus
	winStatus = checkTie()
	return winStatus

def main():
	winStatus = -1
	printBoard()
	print("                  Welcome to Connect 4! Player goes first, and will be represented by an \"X\". Have fun!")
	while winStatus != 0 and winStatus != 1 and winStatus != 2:
		playerTurn()
		printBoard()
		winStatus = checkWin()
		if winStatus == 0 or winStatus == 1 or winStatus == 2:
			break
		computerTurn()
		printBoard()
		winStatus = checkWin()
	if winStatus == 0:
		print("                                             Congratulations! You won!!!")
	elif winStatus == 1:
		print("                                Oh no! The computer beat you! Better luck next time!!!")
	elif winStatus == 2:
		print("                              Game over! All spots are filled, so the game ends in a tie!")

	playAgain = -1
	while playAgain != 0 and playAgain != 1:
		playAgain = intTest("                        Would you like to play again? Enter 0 to play again, or 1 to quit: ")
		if playAgain != 0 and playAgain != 1:
			print("                                               That's not a 0 or a 1!")
		elif playAgain == 0:
			global conArray
			conArray = [
			[" "," "," "," "," "," "," "],
			[" "," "," "," "," "," "," "],
			[" "," "," "," "," "," "," "],
			[" "," "," "," "," "," "," "],
			[" "," "," "," "," "," "," "],
			[" "," "," "," "," "," "," "]
			]
			main()
		elif playAgain == 1:
			break

main()