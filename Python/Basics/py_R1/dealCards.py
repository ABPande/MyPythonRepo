'''
Deck of cards is a list having 
1. Card number (1-52)
2. Card category =  "Spades" "Hearts" "Diamonds" "Clubs"
3. Whether card has been dealt or not
4. Value of card = 2-10 for number cards 11 for ace to be modded by 10 if needed and 10 for face cards
'''
import random
from cards import card 
import 
class dealCards():
	cardNum = 0
	cardCat = 1
	dealt = 2 
	cardVal = 3
	


	def __init__(self):
		self.cards = [[x,int((x-1)/13)+1,False,x] for x in range(1,53)]
		for item in self.cards:
			modRes = item[0]%13
			if modRes >= 2 and modRes <=10:
				item[3] = modRes
			if modRes == 1:
				item[3] = 11
			if (modRes > 10 and modRes <= 13) or (modRes == 0):
				item[3] = 10
		cardsDealt = [0]

	def blackjackDeal():
		player1Cards = ['']	
		player1Cards = player1Cards.append(getCard())
		player1Cards = player1Cards.append(getCard())
		player1Cards.remove ('')
		dealerCards = ['']
		dealerCards = dealerCards.append(getCard())
		dealerCards = dealerCards.append(getCard())
		dealerCards.remove ('')
		return player1Cards, dealerCards

	def getCard():
		cardNum = 0
		while cardNum in self.cardsDealt:
			cardNum = random.randint(1,52)
		cardsDealt.append (cardNum)
		return self.cards[cardNum-1]

	def hit():
		return getCard()

	def shouldHit(dealer,gameMan):
		if gameMan.getSum(dealer) <= 15:
			return true
		return false

