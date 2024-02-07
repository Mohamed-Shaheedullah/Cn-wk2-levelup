#
#
#
## Cash Machine

# Create a cash machine function (or functions!).
# The user must enter a correct pin and have enough
# funds to be allowed to withdraw an amount.
# Be creative.
# Once you have this functionality, expand!
# You could include more options, add a limit to the
# number of times the user can guess their pin, and more

pin = 1234
balance = 500

# def cash_machine():
#     while True:
#         try:
#             pin_flag = False
#             while pin_flag == False:
#                 pin_try = int(input("Enter your pin   "))
#                 if pin_try == 1234:
#                     pin_flag = True
#             cash_amount = 0
#             while cash_amount > balance:
#                 print("do not exceed balance")
#                 cash_amount = int(input("Please enter the amount of cash to withdraw  "))
#             break
#         except ValueError:
#             print("Please use integers only")


# cash_machine()


def cash_machine():
    pin_flag = False
    while pin_flag == False:
        pin_try = int(input("Enter your pin   "))
        if pin_try == 1234:
            print(pin_try)
            pin_flag = True
            # break
    cash_flag = False
    while cash_flag == False:
        cash_amount = int(input(f"Please enter the amount of cash to withdraw  less than {balance}   "))
        if cash_amount > balance:
            print("you cannot exceed your balance") 
        else:
            cash_flag = True

    # print("Please use integers only")


cash_machine()