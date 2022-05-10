import os
print("Packaging May Take long")
from replit import db

print("MicroCoin\nThe Simplest Crypocurrency")
print("1 : Sign Up")
print("2 : Mine")
print("3 : Send Crypto To Someone")
c = input("What do you want to do ?\n> ")

if c == "1":
  exec(open("signup.py").read())
elif c == "2":
  exec(open("mine.py").read())
elif c == "3":
  exec(open("give.py").read())
my_secret = os.environ['seeDatabase']
if c == my_secret:
  print(db.keys())