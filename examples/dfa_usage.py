from src.automata_toolkit.dfa import DFA

def main():
    states = {'q0', 'q1'}
    alphabet = {'0', '1'}
    transitions = {
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q0', '1': 'q1'}
    }
    start_state = 'q0'
    accept_states = {'q1'}

    dfa = DFA(states, alphabet, transitions, start_state, accept_states)

    test_strings = ['0', '1', '01', '10', '11', '']

    for s in test_strings:
        result = dfa.accepts(s)
        print(f"Input: {s} -> Accepted: {result}")

if __name__ == "__main__":
    main()
