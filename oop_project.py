from bank_accounts import * #astreix means all

Izra = BankAccount(1000, "Izra")
Twok = BankAccount(2000, "Twok")

Izra.getBalance()
Twok.getBalance()

Twok.deposit(500)

Izra.withdraw(10000)
Izra.withdraw(10)

Izra.transfer(100, Twok)

#...
Fuluus = InterestRewardsAcct(1000, "Jim")

Fuluus.getBalance()

Fuluus.deposit(100)
Fuluus.transfer(100, Izra)

Naami = SavingsAcct(1000, "Naami")

Naami.getBalance()
Naami.deposit(100)
Naami.transfer(10000, Twok)
Naami.transfer(1000, Twok)