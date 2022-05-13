import time, translate
from replit import db

ps = input("Enter the username of your account \033[33m> ")
print("\033[0m")
pswrd = input("Enter the password of your account \033[33m> ")
print("\033[0m")
wallet = "WAL_"+ps
print("You have ", round(db[wallet], 2), " MicroCoin(s)")

if ("WAL_" + ps) in db:
  if db["PAS_" + ps] == translate.getTo(pswrd):
    startTime = time.time()
    print("You get 2 MicroCoin per minute.")
    input("Press enter to stop mining \033[33m> ")
    print("\033[0m")
    endTime = time.time()
    finalTime = int(endTime - startTime)
    finalTime = int(finalTime) / 30
    if finalTime == 0:
      print("You didn't mine enough to get something !")
      input("Press enter to continue \033[33m> ")
      print("\033[0m")
      exec(open("main.py").read())
    else:
      print("You got \033[33m", round(finalTime, 2), "\033[0m MicroCoin(s)")
      print("= ", translate.toDollar(finalTime), "USD")
      db[wallet] += finalTime
      input("Press enter to continue \033[33m> ")
      print("\033[0m")
      exec(open("main.py").read())