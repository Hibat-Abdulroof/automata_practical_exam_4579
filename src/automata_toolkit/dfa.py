class DFA:
    """A Deterministic Finite Automaton """
    
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        """ Initialize DFA 
            states (set): Set of states (e.g., {'q0', 'q1'})
            alphabet (set): Input symbols (e.g., {'0', '1'})
            transitions (dict): Transition function {state: {symbol: next_state}}
            start_state (str): Initial state
            accept_states (set): Accepting states
        """
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def accepts(self, input_string):
        """ check if the DFA accepts a string."""
        current = self.start_state
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False
            current = self.transitions[current].get(symbol, None)
            if current is None:
                return False
        return current in self.accept_states

def dfa_equivalence(dfa1, dfa2, max_length=20):
    """ DFA equivalence check using BFS.
    Returns True if both DFAs accept the same language.
    """
    # Check alphabet match
    if dfa1.alphabet != dfa2.alphabet:
        return False

    # BFS implementation (avoiding 'queue.Queue')
    queue = [(dfa1.start_state, dfa2.start_state)]
    visited = set(queue)

    while queue:
        s1, s2 = queue.pop(0)

        # Acceptance mismatch = not equivalent
        if (s1 in dfa1.accept_states) != (s2 in dfa2.accept_states):
            return False

        # Explore transitions
        for symbol in dfa1.alphabet:
            next1 = dfa1.transitions[s1].get(symbol, None)
            next2 = dfa2.transitions[s2].get(symbol, None)
            if (next1, next2) not in visited:
                visited.add((next1, next2))
                queue.append((next1, next2))

    return True