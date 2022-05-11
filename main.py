import os
os.system("clear")
my_secret = os.environ['viewDb']
my_secret2 = os.environ['execode']
my_secret3 = os.environ['delAccount']
from replit import db

print("MicroCoin\n---------\nThe Simplest Crypto Currency")
print("1 : Sign Up")
print("2 : Mine")
print("3 : Send MicroCoins To Someone")
print("4 : Show the amount of MicroCoins someone owns")
c = input("\nWhat do you want to do ?\n> ")

if c == "1":
  exec(open("signup.py").read())
elif c == "2":
  exec(open("mine.py").read())
elif c == "3":
  exec(open("give.py").read())
elif c == "4":
  try:
    c = input("Enter the username : ")
    print(db[("WAL_"+c)])
  except KeyError:
    print("This account does not exist")
  finally:
    input("Press enter to continue > ")
    exec(open("main.py").read())
elif c == my_secret:
  print(db.keys())
elif c == my_secret2:
  while True:
    c = input("Code : ")
    if c == "quitItYeahYeah":
      break
    else:
      eval(c)
elif c == my_secret3:
  ps = input("Username > ")
  del db[("WAL_"+ps)]
  del db[("PAS_"+ps)]