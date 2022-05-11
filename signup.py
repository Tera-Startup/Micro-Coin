from replit import db
import translate
print("WARNING : 1 PERSON = 1 ACCOUNT AND NOT MORE")
pseudo = input("Enter your username > ")
print("You can only use the following characters : abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#*")
pswrd = input("Enter your password > ")

fp = "WAL_" + pseudo
fps = "PAS_" + pseudo

db[fp] = 0
db[fps] = translate.getTo(pswrd)

print("You can now mine !")
input("Press enter to continue > ")
exec(open("main.py").read())