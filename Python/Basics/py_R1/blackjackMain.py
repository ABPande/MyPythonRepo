from gameplay import dealCards
from objects import chipManager
from display import display
from gameplay import gameManager

#variables
startVar = 'X'
continueVar = "X"
chipNums = "X"
chipsize = "X"
'''
roundWin = "X" #game manager
gameWin = "X"
'''

#move this code to gamemanager
while (startVar.upper() != 'Y' or startVar.upper() != 'N'):
    startVar = input ("Do you want to start a game of blackjack?")

if startVar == 'Y':			
	gameMan = gameManager()
	chipsize, chipNums = gameMan.initChips()
	
	chipMan = chipManager(chipsize, chipNums)
	cardDealer = dealCards ()
	player1, dealer = cardDealer.blackjackDeal()
	display.show(player1)
	display.show(dealer)
	continueVar = "Y"
	while continueVar.upper() == "Y":
		stayOrHit = 'H'
		val = "1"
		while (stayOrHit.upper() == "H"):
			stayOrHit = input ("Hit or Stay? press H to hit and S to stay")
			if stayOrHit == "H":
				player1 = player1.append(cardDealer.hit(deckOfCards))
				if gameMan.busted(player1)
					gameMan.addRoundWin("Dealer")
					chipMan.transferToDealer (True)
					gameWinner = gameMan.checkWin(chipMan.getP1Chips(),chipMan.getP2Chips())
					display.statusDisplay(gameWinner) 
					break
				display.show(player1)
		if (not gameMan.busted(player1)):
			while (cardDealer.shouldHit(dealer,gameMan)):
				dealer = dealer.append(cardDealer.hit(deckOfCards))
				if gameMan.busted(dealer)
					gameMan.addRoundWin("Player1") 
					chipMan.transferToDealer (False)
					gameWinner = gameMan.checkWin(chipMan.getP1Chips(),chipMan.getP2Chips())
					display.statusDisplay(gameWinner) 
					break
				display.show(dealer)
		if (gameMan.busted(dealer)):
			roundWinner = gameMan.checkRoundWin(player1,dealer)
			gameMan.addRoundWin(roundWinner) 
			if (roundWinner == "Player 1"):
				chipMan.transferToDealer (False)
				print ("Player1 wins round")
			if (roundWinner == "Dealer"):
				print ("Dealer wins round")
				chipMan.transferToDealer (True)
			if (roundWinner == ""):
				print ("Round was a tie")
			gameWinner = gameMan.checkWin(chipMan.getP1Chips(),chipMan.getP2Chips())
			display.statusDisplay(gameWinner) 
			'''if (gameWinner == "Player 1"):
				chipMan.transfer (chipMan.getP2Chips(),chipMan.getP1Chips())
				print ("Player1 wins the game")
			if (gameWinner == "Dealer"):
				print ("Dealer wins the game")
			if (gameWinner == ""):
				print ("Game is a tie") '''
		continueVar = input("Do you want another game? Y/N")
	

