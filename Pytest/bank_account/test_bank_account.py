from Pytest.bank_account.bank_account import BankAccount

def test_deposit():
    account = BankAccount("Alice", 200)
    
    assert account.deposit(50) == 250
    
def test_withdraw():
    account = BankAccount("Bob", 100)
    
    assert account.withdraw(50) == 50
    
def test_withdraw_more_than_balance_error():
    account = BankAccount("Susie", 100)
    
    assert account.withdraw(200) == "Insufficient funds"
    assert account.get_balance() == 100
    
def test_negative_deposit_error():
    account = BankAccount("John", 50)
    
    assert account.deposit(-10) == "Deposit amount must be positive"
    assert account.get_balance() == 50
    
def test_negative_withdrawl_error():
    account = BankAccount("Evan", 75)
    
    assert account.withdraw(-5) == "Withdrawal amount must be positive"
    assert account.get_balance() == 75