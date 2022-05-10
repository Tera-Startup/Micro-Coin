from replit import db
print("WARNING : 1 PERSON = 1 ACCOUNT AND NOT MORE")
pseudo = input("Enter your username > ")
pswrd = input("Enter your password > ")

fp = "WAL_" + pseudo
fps = "PAS_" + pseudo

db[fp] = 0
db[fps] = pswrd

print("You can now mine !")
input("Press enter to continue > ")
exec(open("main.py").read())