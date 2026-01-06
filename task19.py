#Задача 1
def divizion(s):
    listik = s.split()
    x, y = float(listik[0]), float(listik[2])
    try:
        print(x / y)
    except ZeroDivisionError:
        print("ERROR")
s = input()

#Задача 2
def pass_chek(*passwords):
    arr = []
    for password in passwords:
        try:
            check = int(password, 16)
            arr.append(password)
        except ValueError:
            pass
    return arr
print(pass_chek("password", "123456", "abcdef", "bcdefg"))

#Задача 3
olympiad1 = {"name": "Пробная вышка",
"winners": {
"Олеся Олимпиадникova": 594,
"Олег Олимпиадников": 587,
"Онисим Олимпиадников": 581
}
}
olympiad2 = {"name": "Горные воробьи",
"winners": {
"Ольга Олимпиадникова": (20, 20, 19, 20),
"Олеся Олимпиадникова": (19, 19, 20, 20, 17),
"Офелия Олимпиадникова": (20, 20, 20, 20, 13)
}
}

def check_winner(name):
    try:
        ptr1 = olympiad1["winners"][name]
        print(f'[{olympiad1["name"]}] победитель {ptr1}')
    except KeyError:
        print(f'[{olympiad1["name"]}] призёр')
    finally:
        print("----------")
    try:
        ptr2 = olympiad2["winners"][name][4]
        print(f'[{olympiad1["name"]}] победитель {ptr2}')
    except IndexError:
        print(f'[{olympiad1["name"]}] победитель')
    except KeyError:
        print(f'[{olympiad1["name"]}] призёр')
    finally:
        print("----------")
check_winner("Ольга Олимпиадникова")
check_winner("Олеся Олимпиадникова")

#Задача 4
def terrible_program():
    try:
        while(True):
            pass
    except KeyboardInterrupt:
        print("Не дам просто так выйти!")
        terrible_program()
terrible_program()

#Задача 5
class LizardDown(Exception):
    pass
class BarBurn(Exception):
    pass

def bar():
    try:
        mugs = input("Сколько кружек лимонада?").lower()
        if mugs == "ящерица в стакане":
            raise LizardDown
        if mugs == "где туалет?":
            raise BarBurn
        mugs = int(mugs)
        assert mugs < 2
        if mugs <= 0 or mugs >= 100:
            raise ValueError
    except AssertionError:
        print("Слишком много кружек хочешь")
    except LizardDown:
        print("Ящериц нет")
    except BarBurn:
        print("Ура, бар сгорел. Вы вышли из мимуляции")
        return
    print("Приходите ещё!")
    bar()
bar()

