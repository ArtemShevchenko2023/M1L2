import random
russian = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
english = "abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
special = "~`\|.,+-/*!&$#?=@"
passw = input("Добавьте дополнительное слово к паролю если не хотите введите 0")
russ = int(input("Сколько будет русских букв?"))
eng = int(input("Сколько будет английских букв?"))
num = int(input("Сколько будет цифр?"))
spec = int(input("Сколько будет специальных символов?"))
if passw != "0":
    print("Ваш пароль: ", passw, end="")
else:
    print("Ваш пароль: ", end="")
for i in range(russ):
    rus = random.choice(russian)
    print(rus, end="")
for i in range(eng):
    en = random.choice(english)
    print(en, end="")
for i in range(num):
    nu = random.choice(number)
    print(nu, end="")
for i in range(spec):
    spe = random.choice(special)
    print(spe, end="")
print(end="\n")
