def open_account():
    print("New account is created.")
open_account()

def deposit(balance, money):
    print("The money is deposited. The balance is ${0}.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("The money is withdrawn. The balance is ${0}.".format(balance - money))
        return balance - money
    else:
        print("The money can't be withdrawn. The balance is ${0}.".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("The commission is ${0}. The balance is ${1}.".format(commission, balance))