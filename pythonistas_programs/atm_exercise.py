import sys

# Assumptions
# Card has been inserted.

total_balance = 1000
user_pin = 6920

print("Welcome to the Dojlan Bank")
input("Press ENTER to continue")

def atm_verify_pin(pin):
    global user_pin
    if pin == user_pin:
        return True
    else:
        return False

def atm_user_login():
    tries = 0
    while tries < 4:
        pin = int(input('Please Enter Your 4 Digit Pin: '))
        print(pin)
        if atm_verify_pin(pin):
            print("Pin accepted!")
            return True
        else:
            print("Invalid pin")
            tries += 1
    print("To many incorrect tries. Could not log in")
    return False

def atm_user_option():
    answer = input("Would you like to make another transaction y/n?: ").lower()
    if answer == 'y':
        atm_start_menu()
    else:
        sys.exit("Thank you for using Dojlan Bank")

def atm_cash_withdrawal():
    global total_balance
    cash = int(input("Please enter cash amount: "))
    total_balance -= cash
    print(f"New Balance is £{total_balance}")

def atm_cash_deposit():
    global total_balance
    deposit = int(input("How much would you like to deposit: "))
    print(f"You deposited £{deposit}")
    total_balance = total_balance + deposit

def atm_pin_change():
    global user_pin
    current_pin = int(input("Enter current PIN: "))
    if current_pin == user_pin:
        user_pin = input("Enter new PIN: ")
        return user_pin

def atm_print_balance():
    print(f"Your Current Balance is £{total_balance}")

def atm_start_menu():
    print("Main Menu")
    print("Please enter 1: for cash withdrawal.\nPlease enter 2: for deposit.\nPlease enter 3: for change of pin.")
    print("Please enter 4: to check your balance.\nPlease enter 99: to quit.")

def atm_choice():
    choice = int(input("No: "))
    return choice

def main():
    if atm_user_login():
        atm_user_option()
        t=atm_choice()
        while t != 0:
            if t == 99:
                break
            elif t == 1:
                atm_cash_withdrawal()
            elif t == 2:
                atm_cash_deposit()
            elif t == 3:
                atm_pin_change()
            elif t == 4:
                atm_print_balance()
            else:
                print("Invalid Choice")
            print("")
            atm_user_option()
            t=atm_choice()

main()

#Test