from src.automata_toolkit.turing import TuringMachine

def main():
    tm = TuringMachine()

    test_strings = ['11', '111', '1111', '11111']

    for s in test_strings:
        result = tm.run(s)
        print(f"Input: {s} -> Prime length accepted: {result}")

if __name__ == "__main__":
    main()
