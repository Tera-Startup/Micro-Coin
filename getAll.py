from replit import db
import translate

total = 0
tuple = []
for i in db.keys():
        if i.startswith("PAS_"):
            pass
        else:
            tuple.append(i)
for i in tuple:
    total += db[i]
print("There are \033[33m", round(total, 2), "\033[0m MicroCoins in the world !\nThat makes a total of \033[33m", round(translate.toDollar(total), 2), "\033[0mUSD")
input("Press enter to continue \033[33m> ")
print("\033[0m")
exec(open("main.py").read())