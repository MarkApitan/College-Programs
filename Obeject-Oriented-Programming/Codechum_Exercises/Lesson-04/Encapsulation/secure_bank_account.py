# Secure Bank Account - Python
# by CodeChum Admin

# Create a class SecureBankAccount with the following properties and methods:

# Class - SecureBankAccount:

# Private Properties:
# account_number (type: str): The account number of the bank account.
# balance (type: float): The current balance in the bank account.
# pin (type: str): The personal identification number for the account.
# is_locked (type: bool): A flag indicating whether the account is locked or not.

# Constructor:
# __init__(self, account_number: str, initial_balance: float, pin: str): Initializes the account with the provided account_number, initial_balance, and pin. Sets is_locked to False.

# Methods:
# get_account_number(self) -> str: A method that returns the account number.
# get_balance(self) -> float: A method that returns the balance.
# deposit(self, amount: float) -> None: A method that allows depositing money into the account. It checks if the account is locked; if it's locked, no deposit is allowed. If the account is not locked, the deposit increases the balance.
# withdraw(self, amount: float, entered_pin: str) -> str: A method that allows withdrawing money from the account.
# It checks if the account is locked; if it's locked, no withdrawal is allowed.
# If the account is not locked, it checks if the provided PIN matches the account's PIN. If the PIN is correct and the balance is sufficient, it allows the withdrawal and decreases the balance.
# If the balance is insufficient, it rejects the withdrawal and returns a message indicating the result of the withdrawal.
# Possible return messages:
# "Account is locked. Withdrawal not allowed."
# "Incorrect PIN."
# "Insufficient balance for withdrawal."
# "Withdrawal successful. New balance: {balance}"
# Use the appropriate return message for the situation.
# lock_account(self) -> None: A method that locks the account, preventing further withdrawals and deposits. Sets the is_locked property to True.
# __str__(self) -> str: A method that returns a string representation of the account, in the format: account_number - balance - is_locked (e.g., "123123 - P2000.00 - False").

class SecureBankAccount:
    def __init__(self, account_number : str, initial_balance:float, pin:str):
        # Initialize the SecureBankAccount object with the provided account_number, initial_balance, and pin.
        # Set the is_locked property to False.
        self.__account_number = account_number
        self.__balance = initial_balance
        self.__pin = pin 
        self.__is_locked = False

    def get_account_number(self):
        # Return the account number.
        return self.__account_number

    def get_balance(self):
        # Return the balance.
        return self.__balance

    def deposit(self, amount:float):
        # Check if the account is locked.
        # If it's locked, return and do not allow deposit.
        if self.__is_locked:
            return
        # Increase the balance by the deposited amount.
        self.__balance += amount

    def withdraw(self, amount:float, entered_pin: str):
        # Check if the account is locked.
        if self.__is_locked:
            return "Account is locked. Withdrawal not allowed."
        # Check if the entered PIN matches the account's PIN.
        if entered_pin != self.__pin:
            return "Incorrect PIN."
        # Check if the balance is sufficient for withdrawal.
        if amount > self.__balance:
            return "Insufficient balance for withdrawal."
        # If all conditions are met, allow the withdrawal and decrease the balance.
        self.__balance -= amount
        return f"Withdrawal successful. New balance: {self.__balance:.2f}"

    def lock_account(self):
        # Lock the account by setting the is_locked property to True.
        self.__is_locked = True

    def __str__(self):
        # Return a string representation of the account in the format: account_number - balance - is_locked.
        return f"{self.__account_number} - P{self.__balance:.2f} - {self.__is_locked}"