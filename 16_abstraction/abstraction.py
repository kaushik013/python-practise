

# abstraction : 

# ⁡⁣⁢⁣it means hide internal details show only nacessary fetures⁡

# ⁡⁢⁣⁣like example⁡ : 

# ⁡⁣⁣⁢you drive a car you dont see the engine working 

# You use a phone → you don’t know internal circuits.⁡

# 🔵⁡⁣⁣⁢ Why abstraction is used?⁡
# ✔️⁡⁣⁢⁣ Hide complex logic
# ✔️ Force child classes to implement required methods
# ✔️ Improve security
# ✔️ Maintain clean structure⁡


class Account:

    def __init__(self,balance):
        self.balance = balance

    def debit(self,amount):
        self.balance -= amount
        print(f'you bebited {amount} rupee')
        print(f'your acc balance is {self.get_balance()}')

    def cradit(self,amount):
        self.balance += amount
        print(f'your account has been cradit {amount}')
        print(f'your total balance is {self.get_balance()}')

    def get_balance(self):
        return self.balance

acu = Account(10000) 
acu.debit(1000)
acu.cradit(10000)


        

         