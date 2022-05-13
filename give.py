from replit import db
import translate

fromPs = input("Enter your username \033[33m> ")
print("\033[0m")
fromPswrd = input("Enter your password \033[33m> ")
print("\033[0m")
fromPswrdDB = "PAS_"+fromPs
toPs = input("Enter the username of the receiver \033[33m> ")
print("\033[0m")
amounT = input("Enter the amount of MicroCoins you want to send \033[33m> ")
print("\033[0m")
amount = int(amounT)
commission = amount / 100 * 0.99
total = amount + commission
fromWallet = "WAL_"+fromPs
toWallet = "WAL_"+toPs
if db[fromPswrdDB] == translate.getTo(fromPswrd):
  if db[fromWallet] < total:
    print("You don't have enough MicroCoins !")
    input("Press enter to continue \033[33m> ")
    print("\033[0m")
    exec(open("main.py").read())
  else:
    if fromPs == "Krayse":  
      db[fromWallet] -= amount
      db[toWallet] += amount
      #db["WAL_canard"] = (commission / 2)
      #db["WAL_Krayse"] = (commission / 2)
      print("\nYou managed to send ", amount, " MicroCoins to ", toPs)
      input("\nPress enter to continue \033[33m> ")
      print("\033[0m")
      exec(open("main.py").read())
    elif fromPs == "canard":  
      db[fromWallet] -= amount
      db[toWallet] += amount
      #db["WAL_canard"] = (commission / 2)
      #db["WAL_Krayse"] = (commission / 2)
      print("\nYou managed to send ", amount, " MicroCoins to ", toPs)
      input("\nPress enter to continue \033[33m> ")
      print("\033[0m")
      exec(open("main.py").read())
    elif fromPs == "OxBank13":  
      db[fromWallet] -= amount
      db[toWallet] += amount
      #db["WAL_canard"] = (commission / 2)
      #db["WAL_Krayse"] = (commission / 2)
      print("\nYou managed to send ", amount, " MicroCoins to ", toPs)
      input("\nPress enter to continue \033[33m> ")
      print("\033[0m")
      exec(open("main.py").read())
    else:
      db[fromWallet] -= total
      db[toWallet] += amount
      db["WAL_canard"] = (commission / 2)
      db["WAL_Krayse"] = (commission / 2)
      print("\nYou managed to send \033[33m", str(amount), "\033[0m MicroCoins to \033[33m", str(toPs), "\033[0m with \033[33m", str(commission), "\033[0m MicroCoins of commission to the creators !")
      input("\nPress enter to continue \033[33m> ")
      print("\033[0m")
      exec(open("main.py").read())
else:
  print("Wrong password !")
  input("\nPress enter to continue \033[33m> ")
  print("\033[0m")
  exec(open("main.py").read())