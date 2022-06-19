# QUESTION 2
#
# def check_pin(pin, actual_pin):
#     try:
#         pin = int(pin)
#         if pin != actual_pin:
#             raise ValueError("Pin Incorrect")
#
#     except ValueError:
#         try_number = 2
#         while try_number < 4:
#             input_pin_new = int(input("Your pin is incorrect. Please type in your 4 digit pin again."))
#             if input_pin_new == actual_pin:
#                 print("Your pin has been accepted")
#                 return True
#             elif try_number == 3:
#                 raise ValueError("Your pin is incorrect and you have exceeded the max number of tries.")
#             try_number += 1
#
#     else:
#         print("Your pin has been accepted.")
#         return True
#     finally:
#         print("Thank you for using PythonBank")
#
#
# def withdraw_money(withdrawal_amount, bank_balance_now):
#     new_balance = bank_balance_now - withdrawal_amount
#     if new_balance < 0:
#         raise ValueError("You do not have sufficient funds.")
#     print(f"Your new balance is {new_balance}")
#     return new_balance
#
# def main():
#     input_user_pin = input("Please type in your 4 digit pin."))
#     correct_pin = 1234
#     bank_balance = 100
#
#     check_pin(input_user_pin, correct_pin)
#
#     input_withdrawal_amount = int(input("How much would you like to withdraw?"))
#
#     bank_balance = withdraw_money(input_withdrawal_amount,bank_balance)
#
#
# main()

# QUESTION 3 - Question 2 broken down into multiple testable functions.


# def input_pin():
#     return input("What is your pin?")
#
#
# def check_pin(pin, correct_pin):
#     try:
#         pin = int(pin)
#         if pin != correct_pin:
#             raise ValueError("Pin is incorrect")
#     except ValueError:
#         return "Your pin is incorrect. Please try again."
#     else:
#         return "Pin accepted."
#
#
# def money_to_withdraw():
#     return input("How much would you like to withdraw?")
#
#
# def validate_withdrawal(amount):
#     try:
#         amount = int(amount)
#         return amount
#     except ValueError:
#         raise ValueError("You must enter a numerical value with no spaces for withdrawal.")
#
#
# def withdraw_money(amount, balance):
#     new_balance = balance - amount
#     if new_balance < 0:
#         print("You do not have enough money for this withdrawal.")
#         raise ValueError("Insufficient Funds.")
#     if amount < 0:
#         print("You cannot have a negative withdrawal.")
#         raise ValueError("Withdrawal must be a postive number.")
#     print("Withdrawal processed.")
#     return new_balance
#
#
# def print_balance(balance):
#     return f"Your new balance is £{balance}"
#
#
# def main():
#     pin_input = input_pin()
#     correct_pin = 1234
#     account_balance = 100
#
#     status = check_pin(pin_input, correct_pin)
#     print(status)
#     if status == "Your pin is incorrect. Please try again.":
#         pin_input = input_pin()
#         status = check_pin(pin_input, correct_pin)
#         print(status)
#
#     if status == "Your pin is incorrect. Please try again.":
#         pin_input = input_pin()
#         status = check_pin(pin_input, correct_pin)
#         print(status)
#
#     if status == "Your pin is incorrect. Please try again.":
#         print("Pin is incorrect. Maximum number of tries exceeded. Program will now terminate.")
#         raise ValueError("Your pin is incorrect. Maximum number of tries exceed.")
#
#     withdrawal_amount = money_to_withdraw()
#     withdrawal_amount = validate_withdrawal(withdrawal_amount)
#     account_balance = withdraw_money(withdrawal_amount, account_balance)
#     print(print_balance(account_balance))

# for this program to work, run main()











