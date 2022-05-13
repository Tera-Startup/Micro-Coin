from replit import db
import translate
print("WARNING : 1 PERSON = 1 ACCOUNT AND NOT MORE")
pseudo = input("Enter your username \033[33m> ")
print("\033[0m")
print("\nYou can only use the following characters IN YOUR PASSWORD : abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#*")
pswrd = input("Enter your password \033[33m> ")
print("\033[0m")

if "WAL_" + pseudo in db:
  print("This user already exist ;(")
  input("Press enter to continue \033[33m> ")
  print("\033[0m")
  exec(open("main.py").read())
else:
  fp = "WAL_" + pseudo
  fps = "PAS_" + pseudo

db[fp] = 0
db[fps] = translate.getTo(pswrd)

print("You can now mine !")
input("Press enter to continue \033[33m> ")
print("\033[0m")
exec(open("main.py").read())