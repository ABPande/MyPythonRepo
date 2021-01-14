import os
def printBoard (kwargs):
	print (f" {kwargs[0]} | {kwargs[1]} | {kwargs[2]} ")
	print (f"   |   |   ")
	print (f"-----------")
	print (f" {kwargs[3]} | {kwargs[4]} | {kwargs[5]} ")
	print (f"   |   |   ")
	print (f"-----------")
	print (f" {kwargs[6]} | {kwargs[7]} | {kwargs[8]} ")
	print (f"   |   |   ")

def checkWin (ticTacToeList,playChar):
	i=0
	while i < 2:
		if ((ticTacToeList[0]==ticTacToeList[1]==ticTacToeList[2]==playChar[i]) or  
		 (ticTacToeList[3]==ticTacToeList[4]==ticTacToeList[5]==playChar[i]) or 
		 (ticTacToeList[6]==ticTacToeList[7]==ticTacToeList[8]==playChar[i]) or
		 (ticTacToeList[0]==ticTacToeList[3]==ticTacToeList[6]==playChar[i]) or
		 (ticTacToeList[1]==ticTacToeList[4]==ticTacToeList[7]==playChar[i]) or
		 (ticTacToeList[2]==ticTacToeList[5]==ticTacToeList[8]==playChar[i]) or
		 (ticTacToeList[2]==ticTacToeList[4]==ticTacToeList[6]==playChar[i]) or
		 (ticTacToeList[0]==ticTacToeList[4]==ticTacToeList[8]==playChar[i])):
			return i
		i = i+1
	return -1

inpChar  = input ("time to play tictactoe, press 0 to end,any other key to continue")
while inpChar != '0':
	ticTacToeList=['1','2','3','4','5','6','7','8','9']
	playChar = [' ',' ']
	playCount = 0
	inpChar = ' ' 
	while playChar[0] != 'X' and playChar[0] !='O':
		playChar[0] = input ("Player 1 choice of X or O")
	if playChar[0] == 'X':
		playChar[1] = 'O'
	else:
		playChar[1] = 'X'
	gameChar = ' '
	while gameChar != '0':
		gameChar = input(f"player {(playCount % 2)+1} next, choose your location with the numpad (press any key from 1-9), press 0 to exit")
		if gameChar.isnumeric():
			if int(gameChar)>=1 and int(gameChar)<=9 and not (ticTacToeList[int(gameChar)-1] in ('X','O')):
				ticTacToeList[int(gameChar)-1]=playChar[int(playCount)%2]
				playCount = playCount + 1
				os.system('cls')
				printBoard (ticTacToeList)				
				winner = checkWin(ticTacToeList,playChar)
				if winner == 0:
					print ("player 1 wins")
					break
				if winner == 1:
					print ("player 2 wins")
					break
			else:
				print("Bad input, (press any key from 1-9), press 0 to exit")				
		if playCount == 9:
			gameChar = '0'
			print("This was a draw")
			break		
	inpChar = input("Do you want another game? Press 0 to exit, any other key to continue")
