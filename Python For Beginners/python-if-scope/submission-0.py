def pay_bill(balance: int, bill: int) -> int: # Return int type
    if balance >= bill:
        balance = balance - bill # balance -= bill
    return balance

    ''' new_balance = balance
        if balance >= bill:
            new_balance = balance - bill
        return new_balance
    ''' 

# do not modify below this line
print(pay_bill(100, 50))
print(pay_bill(100, 100))
print(pay_bill(100, 150))
