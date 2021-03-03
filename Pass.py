import random as r
alpha=("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
digit=("1234567890")
chars=("~`!@#$%^&*()_+{}:|<>?[];./")
pass_=alpha+digit+chars
password=""
for _ in range(8):
    g=r.choice(pass_)
    password+=g  
print(password)
