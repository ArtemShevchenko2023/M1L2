import random
russian = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
english = "abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
special = "~`\|.,+-/*!&$#?=@"
vopros = int(input("Какая будет длина пароля?"))
passw = input("Добавьте дополнительное слово к паролю если не хотите введите 0")
russ = int(input("Сколько будет русских букв?"))
eng = int(input("Сколько будет английских букв?"))
num = int(input("Сколько будет цифр?"))
spec = int(input("Сколько будет специальных символов?"))
if passw != 0:
    print("Ваш пароль: ", passw, end="")
else:
    print("Ваш пароль: ", end="")
for i in range(vopros):
    pas = random.choice(password)
    print(pas, end="")

