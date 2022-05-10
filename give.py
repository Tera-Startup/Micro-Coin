from replit import db

fromPs = input("Enter your username > ")
fromPswrd = input("Enter your password > ")
fromPswrdDB = "PAS_"+fromPs
toPs = input("Enter the username of the receiver > ")
amounT = input("Enter the amount of MicroCoins you want to send > ")
amount = int(amounT)
#commission = amount / 100 * 0.99
#total = amount + commission
fromWallet = "WAL_"+fromPs
toWallet = "WAL_"+toPs
if db[fromPswrdDB] == fromPswrd:
  if db[fromWallet] < amount:
    print("You don't have enough MicroCoins !")
    input("Press enter to continue > ")
    exec(open("main.py").read())
  else:
    db[fromWallet] -= amount
    db[toWallet] += amount
    #db["WAL_canard"] = (commission / 2)
    #db["WAL_Krayse"] = (commission / 2)
    print("\nYou managed to send ", amount, " MicroCoins to ", toPs)
    input("\nPress enter to continue > ")
    exec(open("main.py").read())
else:
  print("Wrong password !")
  input("\nPress enter to continue > ")
  exec(open("main.py").read())