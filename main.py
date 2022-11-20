from random import randint
a = randint(1, 10)
if a == 10:
    print("大吉です")
if a < 10 and a >7:
    print("中吉です")
if a < 7 and a > 1:
    print("小吉です")
if a == 1:
    print("凶です")
