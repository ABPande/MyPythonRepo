class chipManager():
	def __init__(self,chipsize,chipNums):
		self.player1chips = chipNums
		self.player2chips = chipNums
		self.chipsize = chipsize

	def getP1Chips():
		return self.player1chips

	def getP2Chips():
		return self.player2chips

	def transferToDealer(txToDealer):
		if txToDealer:
			self.player1chips = self.player1chips - self.chipsize
			self.player2chips = self.player2chips + self.chipsize
		else:
			self.player1chips = self.player1chips + self.chipsize
			self.player2chips = self.player2chips - self.chipsize
