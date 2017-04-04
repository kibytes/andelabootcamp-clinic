import unittest
from generate_primes import prime_gen

class TestPrimeGen(unittest.TestCase):

    def test_ten(self):
        #Test if prime numbers are correctly generated.
        self.assertEqual(prime_gen(10), [2, 3, 5, 7])

    def test_prime_gen(self):
        #Test if prime numbers are correctly generated.
        self.assertEqual(prime_gen(20), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_zero(self):
        #Test that zero is not prime.
        self.assertEqual(prime_gen(0), "zero or one cannot be prime.")

    def test_one(self):
        #Test that one is not prime.
        self.assertEqual(prime_gen(1), "zero or one cannot be prime.")

    def test_invalid_type_string_list(self):
        #Test that lists not allowed."""
        self.assertEqual(prime_gen([]), "only integers allowed.")

    def test_only_positive(self):
        #test for negative input
        self.assertEqual(prime_gen(-1), "no primes for integers less than 2.")


if __name__ == "__main__":
    unittest.main()
