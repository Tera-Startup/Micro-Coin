import time
from replit import db

ps = input("Enter the username of the account\nyou want to mine for > ")
pswrd = input("Enter the password of the account\nyou want to mine for > ")
wallet = "WAL_"+ps
print("You have ", db[wallet], " MicroCoin(s)")

if ("WAL_" + ps) in db:
  if ("PAS_" + ps) == pswrd:
    startTime = time.time()
    print("You get 2 MicroCoin per minute.")
    input("Press enter to stop mining > ")
    endTime = time.time()
    finalTime = int(endTime - startTime)
    finalTime = int(finalTime) / 30
    if finalTime == 0:
      print("You didn't mine enough to get something !")
      input("Press enter to continue > ")
      exec(open("main.py").read())
    else:
      print("You got ", finalTime, " MicroCoin(s)")
      db[wallet] += finalTime
      input("Press enter to continue > ")
      exec(open("main.py").read())