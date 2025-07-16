from main import parse_program
import unittest


class ParserTests(unittest.TestCase):
    def test_rc_example(self):
        assert parse_program("(first (list 1 (+ 2 3) 9))") == ["first", ["list", 1, ["+", 2, 3], 9]]
    
    def test_arithmetic_operator_with_int(self):
        assert parse_program("(+ 2 3)") == ["+", 2, 3]
    
    def test_arithmetic_operator_with_float(self):
        assert parse_program("(+ 2 3.5)") == ["+", 2, 3.5]
    
    def test_arithmetic_operator_with_negative_number(self):
        assert parse_program("(+ 2 -3)") == ["+", 2, -3]
    
    def test_boolean_operator(self):
        assert parse_program("(and 1 () 2)") == ["and", 1, [], 2]
    
    def test_empty_list(self):
        assert parse_program("()") == []

    def test_atom_without_parentheses(self):
        assert parse_program("4") == 4
    
    def test_malformed_empty_program(self):
        with self.assertRaises(ValueError):
            parse_program("")
    
    def test_malformed_parentheses_equal_open_and_closed(self):
        with self.assertRaises(ValueError):
            parse_program(")()()(")

    def test_malformed_parentheses_unequal_open_and_closed(self):
        with self.assertRaises(ValueError):
            parse_program("(+ 2 + 3 4))")


if __name__ == '__main__':
        unittest.main()
