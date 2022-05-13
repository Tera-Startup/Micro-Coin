import os
secret = os.environ['outtab']

intab = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#*"
outtab = secret
TABLETO = str.maketrans(intab, outtab)
TABLEFROM = str.maketrans(outtab, intab)

def getTo(self):
  return self.translate(TABLETO)

def getFrom(self):
  return self.translate(TABLEFROM)

change = 0.001
def toDollar(amount):
  v = amount*change
  return v