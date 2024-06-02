# Rational Expression Parser

This project is a parser that recognizes and evaluates arithmetic expressions involving rational numbers. Rational numbers are expressed in the form `numerator|denominator`, such as `2|3` for two-thirds or `12|5` for twelve-fifths. The parser supports the following operations:

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Parentheses for grouping (`(` and `)`)

The program reads arithmetic expressions from standard input, evaluates them, and prints the results. If an invalid expression is encountered, the program will terminate and print the number of correctly evaluated expressions before the error.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/icorvus/rational-expression-parser.git
   cd rational-expression-parser
   ```

1. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

1. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the main.py script and provide arithmetic expressions via standard input:
    ```bash
    python main.py
    ```

1. Example input:
    ```
    2|1+4|1*5|2-18|5
    (2|1+4|1)*5|2-18|5
    four * 5
    ```

1. Example output:
    ```
    42|5
    57|5
    Invalid expression, number of correctly evaluated expressions: 2
    ```

## Code Quality
The code is linted and formatted using `ruff`, a Python code linter and formatter written in Rust.

To lint and format the code, run:
```bash
ruff check .
ruff format .
```

## License

This project is licensed under the MIT License.
