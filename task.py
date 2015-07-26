'''
Parses a Task object out of a description string
'''

class Task:
	price = find Int in description
	variety = [windows, pw, roof, tip]

	tax = 0

	def init (self, description):
		self.name = extractNameFromDescription()
		self.price = extractPriceFromDescription()
		self.type = setType()
		self.tax = setTax()

	def setTax(self, description):
		taxable = False
		if variety is not windows and not tip:
			taxable = True
		else:
			taxable = False

		taxRate = taxRateFromLocation()
		if taxable == True:
			taxMultiplier = taxRate
			tax = (price * taxMultiplier)
		else:
			tax = 0

		return tax

	def taxRateFromLocation():
		if location == WestSeattle:
			taxRate = 0.96
		elif location == MercerIsland:
			taxRate = 0.95
		elif location == Bellevue:
			taxRate = 0.95
		return taxRate
