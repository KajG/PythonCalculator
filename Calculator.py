import sys

class calculate():
	def __init__(self):
		self.startValue = sys.argv[1]

		self.main()

	def main(self):
		first = raw_input("Fill in the first integer: ")
		one = self.checkInput(first)

		second = raw_input("Fill in the second integer: ")
		two = self.checkInput(second)

		if self.startValue == "add":
			answer = self.add(one,two)
			print one," + ", two, " = " ,answer
			sys.exit("Done")

		if self.startValue == "multiply":
			answer = self.multiply(one,two)
			print one, " * ", two, " = ", answer
			sys.exit("Done")

		if self.startValue == "subtract":
			answer = self.subtract(one,two)
			print one, " - ", two, " = ", answer
			sys.exit("Done")

	def add(self,num1,num2):
		ans = (num1 + num2)
		return ans

	def multiply(self,num1,num2):
		ans = (num1 * num2)
		return ans

	def subtract(self,num1,num2):
		ans = (num1 - num2)
		return ans

	def checkInput(self,theInput):
		if "," in theInput:
			theInput = theInput.replace(",",".")
		try:
			temp = int(theInput)
			return temp
		except:
			try:
				temp = float(theInput)
				return temp
			except:
				print "Only integers and floats are allowed, the input is a string!"
				self.main()


var = calculate()
