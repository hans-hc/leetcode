class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.n = len(balance)

    # check if account number exists, numbers go from 1-n
    def _valid(self, account: int) -> bool:
        return 1 <= account <= self. n

    # Transfer:
    # Do both accounts exist? If not, false
    # Does account 1 have enough money? if not, false
    # Subtract from account 1, add to account 2, return true
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self._valid(account1) or not self._valid(account2):
            return False
        if self.balance[account1 - 1] < money:
            return False
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True
        
    # Deposit:
    # Does the account exist? if not, False
    # Add money, return True
    def deposit(self, account: int, money: int) -> bool:
        if not self._valid(account):
            return False
        self.balance[account-1] += money
        return True

    # Withdraw:
    # Does the account exist? if not, return false
    # Does the account have enough money? If not, return false
    # Subtract the money, return true
    def withdraw(self, account: int, money: int) -> bool:
        if not self._valid(account):
            return False
        if self.balance[account - 1] < money:
            return False
        self.balance[account - 1] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)