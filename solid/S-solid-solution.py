import datetime

TRANSACTION_LOG_FILE = "transactions.log"


class TransactionWriteLogService:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def write_log(self, transaction_type, amount):
        with open(TRANSACTION_LOG_FILE, "a") as log_file:
            log_file.write(
                f"{datetime.datetime.now()}: {transaction_type} {amount} into {self.account_number}\n"
            )


class GenerateStatementService:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def generate_statement(self):
        statement = f"Statement for Account: {self.account_number}\nBalance: {self.balance}\n"
        print(statement)
        with open("statements.log", "a") as stmt_file:
            stmt_file.write(f"{datetime.datetime.now()}: Generated statement for {self.account_number}\n")
        print(f"Sending email with statement for account {self.account_number}...")


class WithdrawService:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        print(f"Sending email notification: {amount} withdrawn from account {self.account_number}.")


class DepositService:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print(f"Sending email notification: {amount} deposited into account {self.account_number}.")


class Account:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def __repr__(self):
        return f"{self.account_number} has {self.balance} balance"


class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account = Account(account_number, balance)

    def deposit(self, amount):
        service = DepositService(self.account.account_number, self.account.balance)
        service.deposit(amount)
        transaction_log_service = TransactionWriteLogService(self.account.account_number, self.account.balance)
        transaction_log_service.write_log("Deposited", amount)

    def withdraw(self, amount):
        service = WithdrawService(self.account.account_number, self.account.balance)
        service.withdraw(amount)
        transaction_log_service = TransactionWriteLogService(self.account.account_number, self.account.balance)
        transaction_log_service.write_log("Withdrew", amount)
        print(f"Sending email notification: {amount} withdrawn from account {self.account.account_number}.")

    def generate_statement(self):
        service = GenerateStatementService(self.account.account_number, self.account.balance)
        service.generate_statement()
        transaction_log_service = TransactionWriteLogService(self.account.account_number, self.account.balance)
        transaction_log_service.write_log("Generated statement", 0)
