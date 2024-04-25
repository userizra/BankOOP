from bank_accounts import * #astreix means all

Izra = BankAccount(1000, "Izra")
Twok = BankAccount(2000, "Twok")

Izra.getBalance()
Twok.getBalance()

Twok.deposit(500)

Izra.withdraw(10000)