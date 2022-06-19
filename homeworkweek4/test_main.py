import unittest
from main import check_pin, validate_withdrawal, withdraw_money, print_balance


class TestCheckPin(unittest.TestCase):

    def test_same_pin(self):
        expected = "Pin accepted."
        result = check_pin("1234",1234)
        self.assertEqual(expected, result)

    def test_different_pin(self):
        expected = "Your pin is incorrect. Please try again."
        result = check_pin("1234", 2345)
        self.assertEqual(expected, result)

    def test_string_pin(self):
        expected = "Your pin is incorrect. Please try again."
        result = check_pin("hello", 1234)
        self.assertEqual(expected, result)


class TestValidateWithdrawal(unittest.TestCase):

    def test_string_withdrawal(self):
        with self.assertRaises(ValueError):
            validate_withdrawal("twenty")

    def test_int_withdrawal(self):
        expected = 20
        result = validate_withdrawal("20")
        self.assertEqual(expected,result)


class TestWithdrawMoney(unittest.TestCase):

    def test_draw_too_much(self):
        with self.assertRaises(ValueError):
            withdraw_money(150,75)

    def test_positive_draw(self):
        expected = 150
        result = withdraw_money(50,200)
        self.assertEqual(expected, result)

    def test_negative_draw(self):
        with self.assertRaises(ValueError):
            withdraw_money(-20,75)


class TestPrintBalance(unittest.TestCase):

    def test_print_balance(self):
        expected = "Your new balance is £60"
        result = print_balance(60)
        self.assertEqual(expected,result)


if __name__ == '__main__':
    unittest.main()
