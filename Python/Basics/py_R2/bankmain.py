class Customer():
	customerID = 0
	def __init__ (self, name):
		self.name = name
		Customer.customerID = Customer.customerID + 1
		
	def getCustomerName(self):
		return self.name

	def getCustomerID(self):
		return self.customerID

class BusinessCustomer(Customer):
	def __init__ (self, name, TaxID):
		Customer.__init__(self, name)
		self.customerID = Customer.customerID
		self.TaxID = TaxID
	def __str__(self):
		return ("Business Customer: " + str(self.customerID) + " with TaxID: " + str(self.TaxID))
	def getCustomerID(self):
		return self.customerID

class IndividualCustomer(Customer):
	def __init__ (self, name, age, gender):
		Customer.__init__(self, name)
		self.customerID = Customer.customerID
		self.age = age
		self.gender = gender
	def __str__(self):
		return ("Individual Customer: " + str(self.customerID) + " of name: " + self.name + " of age: " + str(self.age) + " of gender: " + self.gender)
	def getCustomerID(self):
		return self.customerID

class BankAccount():
	initialBalance = 500
	creditLimit = 500
	def __init__(self, customer, deposit):
		self.balance = initialBalance + deposit 
		self.customer = customer

	def withdraw(self, withdrawal):
		if self.balance > withdrawal:
			self.balance = self.balance - withdrawal
			return withdrawal
		else:
			print ("Insufficient Money")
			return 0

	def deposit (self, amount):
		self.balance = self.balance + amount

IndividualCustomer1 = IndividualCustomer("Abhijit", 32, "male")
BusinessCustomer1 = BusinessCustomer("RML", 1231412)
for item in [IndividualCustomer1,BusinessCustomer1]:
	print (str(item))

