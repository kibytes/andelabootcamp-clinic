import unittest

def calc_loan_pay(A, T, R):
	return int(A * (R/100) * (T/12)) + A

def work():
	A = float(input("Enter the loan amount: "))
	T = float(input("Enter the loan period: "))
	R = float(input("Enter the interest rate: "))

	print calc_loan_pay (A, T, R)

#work()

class CalcLoanPayTestcase(unittest.TestCase):
	def testdddddcalc_loan_pay(self):
		self.assertEqual(calc_loan_pay(100000, 12, 12),(112000))

if __name__ == '__main__':
	unittest.main()