from random import randint
a = randint(1, 10)
if a == 10:
    i = "大吉"
    pyscript.write("kekka",i)
if a < 10 and a >7:
    i = "中吉"
    pyscript.write("kekka",i)
if a < 7 and a > 1:
    i = "小吉"
    pyscript.write("kekka",i)
if a == 1:
    i = "凶"
    pyscript.write("kekka",i)
