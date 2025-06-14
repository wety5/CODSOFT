import random
import string
n=int(input("Enter the password length"))
s=""
s=string.ascii_letters+string.punctuation+string.digits
lt=list(s)
random.shuffle(lt)
pwd=[]
for i in range(n):
      c=random.choice(lt)
      pwd.append(c)
print("".join(pwd))
