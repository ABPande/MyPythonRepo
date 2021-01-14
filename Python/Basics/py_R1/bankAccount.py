
class BankAccount():
	accountID = 0
	def __init__ (self, customerID, savingsBalance, checkingBalance, overdraftLimit):
		self.customerID = customerID
		self.accountID = BankAccount.accountID + 1
		BankAccount.accountID = self.accountID
		self.savingsBalance = savingsBalance
		self.checkingBalance = checkingBalance
		self.overdraftLimit = overdraftLimit
		self.overdraftAvailable = overdraftLimit
		self.charges = 0
		
	def withdraw (amount):
		if amount > (self.checkingBalance + self.savingBalance + self.overdraftLimit):
			print("amount is greater than allowed")
		else 
			if amount <= self.checkingBalance:
				self.checkingBalance = self.checkingBalance - amount
				print ("amount withdrawn \nChecking Balance = {self.checkingBalance}\n SavingsBalance = {self.savingsBalance} \n Overdraft available = {self.overdraftAvailable}")
			else :
				if amount > self.checkingBalance:
					self.checkingBalance = 0
					amount = amount - self.checkingBalance
					if amount <= self.savingsBalance:
						self.savingsBalance = self.savingsBalance - amount
						print ("amount withdrawn \nChecking Balance = {self.checkingBalance}\n SavingsBalance = {self.savingsBalance} \n Overdraft available = {self.overdraftAvailable}")
					else:
						if amount > self.savingsBalance:
							self.savingsBalance = 0
							amount = amount - self.savingsBalance
							if amount <= self.overdraftAvailable:
								self.overdraftAvailable = self.overdraftAvailable - amount
								print ("amount withdrawn \nChecking Balance = {self.checkingBalance}\n SavingsBalance = {self.savingsBalance} \n Overdraft available = {self.overdraftAvailable}")
