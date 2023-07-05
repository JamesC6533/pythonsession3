# The Account class is defined as the base class for different types of accounts
class Account:
    # It has a class variable count to keep track of the number of accounts created
    count = 0

    # The __init__ method is a constructor that initializes the account_number,
    # and account_holder instance variables.
    def __init__(self, account_number, account_holder):
        self._account_number = account_number
        self._account_holder = account_holder
        Account.count += 1

    # The @property decorators are used to define getter methods for the account_number,
    # and account_holder attributes.
    @property
    def account_number(self):
        return self._account_number

    @property
    def account_holder(self):
        return self._account_holder

    # The deposit and withdraw methods are defined as placeholders,
    # and will be overridden in the derived classes.
    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    # The close_account method decreases the account count by one
    @classmethod
    def close_account(cls):
        cls.count -= 1

    # The get_count method returns the total number of accounts created.
    @classmethod
    def get_count(cls):
        return cls.count


# The SavingsAccount class is derived from the Account class,
# representing a type of savings account.
class SavingsAccount(Account):
    # The __init__ method initializes the account number, account holder, and interest rate.
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self._interest_rate = interest_rate

    # The interest_rate method is a getter for the interest rate attribute
    @property
    def interest_rate(self):
        return self._interest_rate

    # The deposit and withdraw methods are overridden to provide specific functionality,
    # for a savings account.
    def deposit(self, amount):
        print("Depositing {} into Savings Account.".format(amount))

    def withdraw(self, amount):
        print("Withdrawing {} from Savings Account.".format(amount))


# The CurrentAccount class is derived from the Account class,
# representing a type of current account.
class CurrentAccount(Account):
    # The __init__ method initializes the account number, account holder, and overdraft limit
    def __init__(self, account_number, account_holder, overdraft_limit):
        super().__init__(account_number, account_holder)
        self._overdraft_limit = overdraft_limit

    # The overdraft_limit method is a getter for the overdraft limit attribute.
    @property
    def overdraft_limit(self):
        return self._overdraft_limit

    # The deposit and withdraw methods are overridden to provide specific functionality,
    # for a current account.
    def deposit(self, amount):
        print("Depositing {} into Current Account.".format(amount))

    def withdraw(self, amount):
        print("Withdrawing {} from Current Account.".format(amount))


# The FixedDepositAccount class is derived from the Account class,
# representing a type of fixed deposit account.
class FixedDepositAccount(Account):
    # The __init__ method initializes the account number,
    # account holder, deposit amount, and term.
    def __init__(self, account_number, account_holder, deposit_amount, term):
        super().__init__(account_number, account_holder)
        self._deposit_amount = deposit_amount
        self._term = term

    # The deposit_amount and term methods are getters for their respective attributes.
    @property
    def deposit_amount(self):
        return self._deposit_amount

    @property
    def term(self):
        return self._term

    # The deposit method is overridden to provide specific functionality,
    # for a fixed deposit account, printing a deposit message.
    def deposit(self, amount):
        print("Depositing {} into Fixed Deposit Account.".format(amount))

    # The withdraw method is overridden to indicate that withdrawal is not allowed,
    # from a fixed deposit account.
    def withdraw(self, amount):
        print("Withdrawal is not allowed from Fixed Deposit Account.")


if __name__ == '__main__':
    savings_account = SavingsAccount("SA-001", "James Cotterill", 2.5)
    current_account = CurrentAccount("CA-001", "Amber MacDonald", 10000)
    fixed_deposit_account = FixedDepositAccount("FDA-001", "Andrew Forshaw", 50000, 12)

    # A loop iterates over the created accounts.
    for account in savings_account, current_account, fixed_deposit_account:
        # The deposit and withdraw methods are called on each account,
        # and the appropriate messages are printed.
        account.deposit(1000)
        account.withdraw(500)
        print()

    # get_count method is called on the Account class to print the total number,
    # of accounts created.
    print("Total number of accounts:", Account.get_count())
