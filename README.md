# Automata Theory Practical Exam 4579
- Section number : 6

## 1. Deterministic Finite Automata (DFA) Implementation

### Task Solved:
Implementation of a DFA that can:
- Test string acceptance
- Check equivalence between two DFAs

### How to Run:

# Run DFA example
python -m examples.dfa_usage

# Run DFA tests
python -m pytest tests/test_dfa.py -v
python -m pytest tests/test_dfa.py -v

### Source Code (src/automata_toolkit/dfa.py)

---

## 2. Turing Machine Implementation

### Task Solved:
Turing Machine that accepts unary strings where the string length is a prime number

### How to Run:

# Run Turing Machine example
python -m examples.turing_usage

# Run Turing Machine tests
python -m pytest tests/test_turing.py -v
python -m pytest tests/test_turing.py -v

### Source Code (src/automata_toolkit/turing.py)

---

## 3. Testing Framework

### Task Solved:
Unit tests for both DFA and Turing Machine implementations

### How to Run:

# Run all tests
python -m pytest

# Run specific test suite
python -m pytest tests/test_dfa.py
python -m pytest tests/test_turing.py

### Example Test Case (tests/test_dfa.py)
---

## 4. Examples

### Task Solved:
Demonstration scripts showing usage of both automata implementations

### How to Run:

python -m examples.dfa_usage
python -m examples.turing_usage


---
## 5. Requirements

### Dependencies:

# requirements.txt
pytest==7.4.0

### Installation:
pip install -r requirements.txt


---
## Project Structure

AUTOMATA_PRACTICAL_EXAM_4579_ID/
│
├── .pytest_cache/          # Pytest cache directory (auto-generated)
├── .venv/                  # Python virtual environment (should be in.gitignore)
├── .vscode/                # VS Code configuration (should be in.gitignore)
│
├── examples/               # Example usage scripts
│   ├── __pycache__/        # Python bytecode cache
│   ├── dfa_usage.py        # DFA usage examples
│   └── turing_usage.py     # Turing Machine usage examples
│
├── src/                    # Source code root
│   └── automata_toolkit/   # Main package
│       ├── __pycache__/    # Python bytecode cache
│       ├── __init__.py     # Package initialization
│       ├── dfa.py          # DFA implementation
│       └── turing.py       # Turing Machine implementation
│
├── tests/                  # Test cases
│   ├── __pycache__/        # Python bytecode cache
│   ├── test_dfa.py         # DFA tests
│   └── test_turing.py      # Turing Machine tests
│
├── LICENSE                 # Project license
├── pyproject.toml          # Build system configuration
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
