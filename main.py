import random
password = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
vopros = int(input("Какая будет длина пароля?"))
print("Ваш пароль: ", end="")
for i in range(vopros):
    b = random.choice(password)
    print(b, end="")
print(end="\n")