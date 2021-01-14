'''
Deck of cards is a list having 
1. Card number (1-52)
2. Card category =  "Spades" "Hearts" "Diamonds" "Clubs"
3. Whether card has been dealt or not
4. Value of card = 2-10 for number cards 11 for ace to be modded by 10 if needed and 10 for face cards
'''
class gameManager():

	def __init__(self):
		winnerList = ['']

	def initChips():
		while chipNums == "X":
			chipNums = input ("Enter number of chips 50-500")
			if (chipNums >= 50 and chipNums <= 500):
				chipNums = int (chipNums)
		while chipsize == "X":
			chipsize = input ("Enter chip size 10-50")
			if (chipsize >= 10 and chipsize <= 50):
				chipsize = int (chipsize)
		return chipsize, chipNums

	def busted(player):
		if getSum(player) > 21:
			return True

	def addRoundWin(winner):
		winnerList.append(winner)

	def checkRoundWin(player1,dealer):
		if 21 >= getSum(player1) > getSum(dealer):
			return "Player 1"
		if 21 >= getSum(dealer) > getSum(player1):
			return "Dealer"
		if getSum(dealer) == getSum(player1):
			return ""

	def checkGameWin(p1Chips,p2Chips):
		if p1Chips == 0: 
			print ("Dealer wins")
		if p2Chips == 0:
			print ("Player 1 wins")


	def getSum(player):
		sum = 0
		for item in player:
			if item[3] == 11:
				if sum + item[3] > 21:
					sum = sum + 1
			else:
				sum = sum + item[3]
		return sum