from typing import List, Union

"""
Lisp parser

Write code that takes some Lisp code and returns an abstract syntax tree.
The AST should represent the structure of the code and the meaning of each Element.
For example, if your code is given "(first (list 1 (+ 2 3) 9))",
it could return a nested array like ["first", ["list", 1, ["+", 2, 3], 9]].

During your interview, you will pair on writing an interpreter to run the AST.
You can start by implementing a single built-in function (for example, +) and add more if you have time.
"""

# Type definitions
type AST = Union[List, Atom]
type Atom = Union[Number, Symbol]
type Number = float
type Symbol = str

"""
Convert a Lisp program into an abstract syntax tree.
"""
def parse_program(program: str) -> AST:
    tokens = _tokenize(program)
    if not _is_program_well_formed(tokens):
        raise ValueError("program is malformed")
    return _parse_tokens(tokens)

def _tokenize(program: str) -> List[str]:
    whitespaced_input = program.replace("(", " ( ").replace(")", " ) ")
    return whitespaced_input.split()

def _is_program_well_formed(tokens: List[str]) -> bool:
    if len(tokens) == 0:
        return False
    stack_count = 0
    for token in tokens:
        match token:
            case "(":
                stack_count += 1
            case ")":
                if stack_count == 0:
                    return False
                stack_count -= 1
    return stack_count == 0

def _parse_tokens(tokens: List[str]) -> AST:
    while len(tokens) > 0:
        token = tokens.pop(0)
        match token:
            case "(":
                ast = []
                while len(tokens) > 0 and tokens[0] != ")":
                    ast.append(_parse_tokens(tokens))
                tokens.pop(0)
                return ast
            case x:
                try:
                    return float(x)
                except ValueError:
                    return x
