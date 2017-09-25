import unittest
from string_sum import ssum

class Test(unittest.TestCase):
    def test_no_numbers(self):
        self.assertEqual(ssum(''), 0, msg="Empty String does not returns 0")

    def test_one_number(self):
        self.assertEqual(ssum('1'), 1, msg="\"1\" String does not returns 1")
        self.assertEqual(ssum('2'), 2, msg="\"2\" String does not returns 2")

    def test_multiple_number(self):
        self.assertEqual(ssum('1,2'), 3, msg="\"1,2\" String does not returns 3")
        self.assertEqual(ssum('1,2,7'), 10, msg="\"1,2,7\" String does not returns 10")

    def test_new_line_in_inputs(self):
        self.assertEqual(ssum('1\n2'), 3, msg="\"1\\n2\" String does not returns 3")
        self.assertEqual(ssum('1\n2,3'), 6, msg="\"1\\n2,3\" String does not returns 6")

    def test_new_delimeters(self):
        self.assertEqual(ssum('//-\n1-2'), 3, msg="\//-\n1-2\" String does not returns 3")
        self.assertEqual(ssum('//;\n1;2'), 3, msg="\//;\n1;2\n3\" String does not returns 6")

    def test_assertion_negative(self):
        with self.assertRaises(ValueError) as err:
            ssum('-2')
        self.assertEqual(err.exception.args, ("negatives not allowed", [-2]))

        with self.assertRaises(ValueError) as err:
            ssum('-2,-4')
        self.assertEqual(err.exception.args, ("negatives not allowed", [-2,-4]))

    def test_ignore_bigger_then_100_number(self):
        self.assertEqual(ssum('1,2,700'), 3, msg="\"1,2,700\" String does not returns 3")



if __name__ == '__main__':
    unittest.main()
