import unittest
from src.automata_toolkit.dfa import DFA, dfa_equivalence

class TestDFA(unittest.TestCase):
    def setUp(self):
        self.dfa1 = DFA(
            states={'q0', 'q1'},
            alphabet={'0', '1'},
            transitions={
                'q0': {'0': 'q0', '1': 'q1'},
                'q1': {'0': 'q0', '1': 'q1'}
            },
            start_state='q0',
            accept_states={'q1'}
        )
        self.dfa2 = DFA(
            states={'p0', 'p1'},
            alphabet={'0', '1'},
            transitions={
                'p0': {'0': 'p0', '1': 'p1'},
                'p1': {'0': 'p0', '1': 'p1'}
            },
            start_state='p0',
            accept_states={'p1'}
        )
        self.dfa3 = DFA(
            states={'r0', 'r1'},
            alphabet={'0', '1'},
            transitions={
                'r0': {'0': 'r1', '1': 'r0'},
                'r1': {'0': 'r0', '1': 'r1'}
            },
            start_state='r0',
            accept_states={'r1'}
        )

    def test_accepts(self):
        self.assertTrue(self.dfa1.accepts('1'))
        self.assertTrue(self.dfa1.accepts('01'))
        self.assertFalse(self.dfa1.accepts('0'))
        self.assertFalse(self.dfa1.accepts(''))

    def test_equivalence(self):
        self.assertTrue(dfa_equivalence(self.dfa1, self.dfa2))
        self.assertFalse(dfa_equivalence(self.dfa1, self.dfa3))

if __name__ == '__main__':
    unittest.main()