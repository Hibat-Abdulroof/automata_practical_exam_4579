from src.automata_toolkit.turing import TuringMachine
import unittest

class TestTuringMachine(unittest.TestCase):
    def setUp(self):
        self.tm = TuringMachine()
    
    def test_prime_lengths(self):
        primes = [2, 3, 5, 7, 11]  # Test first few primes
        for p in primes:
            with self.subTest(prime=p):
                input_str = "1" * p
                self.assertTrue(self.tm.run(input_str), f"Should accept prime length {p}")
    
    def test_non_prime_lengths(self):
        non_primes = [1, 4, 6, 8, 9, 10]  # Test non-primes
        for np in non_primes:
            with self.subTest(non_prime=np):
                input_str = "1" * np
                self.assertFalse(self.tm.run(input_str), f"Should reject non-prime length {np}")
    
    def test_edge_cases(self):
        self.assertFalse(self.tm.run(""), "Empty string should be rejected")
        self.assertFalse(self.tm.run("1"), "Length 1 should be rejected")

if __name__ == "__main__":
    unittest.main()