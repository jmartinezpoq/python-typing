from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Tuple

class Bank(ABC):
    @abstractmethod
    def withdraw(self, amount: int) -> None:
        ...

class BankAccount(Bank):
    def __init__(self, initial_balance: int = 0) -> None:
        self.balance = initial_balance
    def deposit(self, amount: int) -> None:
        self.balance += amount
    def withdraw(self, amount: int) -> None:
        self.balance -= amount

class AnotherBankAccount(Bank):
    def withdraw(self, amount: int) -> None:
        pass

    def get_data_bank(self) -> Optional[str]: #Union[X, None]
        return None

my_account: Bank = BankAccount(15)
my_account.withdraw(5)

my_other_account: AnotherBankAccount = AnotherBankAccount() 

#data_bank: str
data_bank = my_other_account.get_data_bank()

# if isinstance(data_bank, str):
#     data_bank.split(" ")

assert type(data_bank) == str
data_bank.split(" ")

OUR_DICT = Dict[str, Dict[str,List[Dict[str,int]]]]

test_dict:OUR_DICT = {
    "1": {
        "a": [
            {"f": 1}
        ]
    }
}
