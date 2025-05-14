class TuringMachine:
    """ Turing Machine to accept unary strings of prime length"""

    def __init__(self):
        self.tape = []
        self.head = 0
        self.state = "start"
        self.blank = "B"

    def run(self, input_str):
        length = len(input_str)
        if length <= 1:
            return False  # Not prime

        for d in range(2, length):
            if self._is_divisible(length, d):
                return False  # Found a divisor

        return True  # No divisor found → Prime

    def _is_divisible(self, n, d):
        """
        Simulate whether d divides n using repeated subtraction (like a TM would do).
        Example: is 7 divisible by 3?
        Subtract 3 → 4 → subtract 3 → 1 → not divisible
        """
        count = 0
        while count + d <= n:
            count += d
        return count == n