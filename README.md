# Recurse Center Programming Interview

I've chosen to implement the Lisp Parser task:
> Write code that takes some Lisp code and returns an abstract syntax tree. The AST should represent the structure of the code and the meaning of each token. For example, if your code is given `"(first (list 1 (+ 2 3) 9))"`, it could return a nested array like `["first", ["list", 1, ["+", 2, 3], 9]]`.

> During your interview, you will pair on writing an interpreter to run the AST. You can start by implementing a single built-in function (for example, `+`) and add more if you have time.

This is implemented in `main.py` and tested in `test_main.py`. Note that you will need at least Python 3.10 to get `match` to work.
