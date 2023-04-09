import random
password = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
vopros = int(input("Какая будет длина пароля?"))
passw = input("Добавьте дополнительное слово к паролю если не хотите введите 0")
if passw != 0:
    print("Ваш пароль: ", passw, end="")
else:
    print("Ваш пароль: ", end="")
for i in range(vopros):
    pas = random.choice(password)
    print(pas, end="")
print(end="\n")
