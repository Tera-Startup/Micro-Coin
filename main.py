# MicroCoin 1.2 by Tera #

"""
Copyright © Tera, Inc. 2022.
This software is a creation of Gustave Dufresne Walter (a.k.a. Krayse)
and Jules Auburtin (a.k.a. canard).
It belongs to its rightful owner, and shall not be used in copy or something.
If you want to use that project in a video, or something destined to be posted on the Internet, please ask us on jules.auburt1@protonmail.com .
"""
import os
os.system("clear")
my_secret = os.environ['viewDb']
my_secret2 = os.environ['execode']
my_secret3 = os.environ['delAccount']
my_secret4 = os.environ['addCoins']
from replit import db

print("\033[0;43;30mMicroCoin\033[0m\n\033[33m-\033[0m-\033[33m-\033[0m-\033[33m-\033[0m-\033[33m-\033[0m-\033[33m-\033[0m\n\033[4;33mThe Simplest Crypto Currency\033[0;33m\nCopyright © Tera, Inc. 2022\nYou like it ? Give us MicroCoins ! (our usernames are 'Krayse' and 'canard'\033[0m")
print("\033[33m-\033[0m-\033[33m-\033[0m-\033[33m-\033[0m-\033[33m-\033[0m-\033[33m-\033[0m")
print("\033[33m1\033[0m : Sign Up")
print("\033[33m-\033[0m-\033[33m-\033[0m-\033[33m-\033[0m-\033[33m-\033[0m-\033[33m-\033[0m")
print("\033[33m2\033[0m : Mine")
print("\033[33m-\033[0m-\033[33m-\033[0m-\033[33m-\033[0m-\033[33m-\033[0m-\033[33m-\033[0m")
print("\033[33m3\033[0m : Send MicroCoins To Someone")
print("\033[33m-\033[0m-\033[33m-\033[0m-\033[33m-\033[0m-\033[33m-\033[0m-\033[33m-\033[0m")
print("\033[33m4\033[0m : Show the amount of MicroCoins someone owns")
print("\033[33m-\033[0m-\033[33m-\033[0m-\033[33m-\033[0m-\033[33m-\033[0m-\033[33m-\033[0m")
print("\033[33m5\033[0m : Show total of MicroCoins in the world")
c = input("\nWhat do you want to do ?\n\033[33m> ")
print("\033[0m")

if c == "1":
  exec(open("signup.py").read())
elif c == "2":
  exec(open("mine.py").read())
elif c == "3":
  exec(open("give.py").read())
elif c == "4":
  try:
    c = input("Enter the username : ")
    print(round(db[("WAL_"+c)], 2), "MicroCoin(s)")
  except KeyError:
    print("This account does not exist")
  finally:
    input("Press enter to continue \033[33m> ")
    print("\033[0m")
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
  ps = input("Username \033[33m> ")
  print("\033[0m")
  del db[("WAL_"+ps)]
  del db[("PAS_"+ps)]
elif c == "5":
    exec(open("getAll.py").read())
elif c == my_secret4:
  wallet = "WAL_" + input("Username : ")
  db[wallet] += int(input("Enter the amount : "))