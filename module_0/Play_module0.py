print("Игра крестики-нолики")
print("Формат ввода: x y")
print("x - строки, y - столбцы")

# подход с двумерным массивом - поле 3 списка по 3 элемента
field = [[" "] * 3 for i in range(3)]

def show():
    '''Фрагмент кода для визуализации игрового поля'''
    print(f"  0 1 2")
    for i in range(3):
        print(f"{i} {field[i][0]} {field[i][1]} {field[i][2]}")
show()

def ask():
    '''Спрашиваем у пользователя куда ставить'''
    while True:
        value = input("     Ваш ход: ").split()
        if len(value) != 2:
            print("Введите две координаты")
            continue

        x,y = value

        if not(x.isdigit()) or not(y.isdigit()):
            print("Введены не числа")
            continue

        x,y = int(x), int(y)

        if 0 <= x <= 2 and 0 <= y <= 2:
            if field[x][y] == " ":
                # возвращаем кортеж
                return x,y
            else:
                print("Клетка занята!")
        else:
            print(" Координаты вне диапазона!")

def winning_combination():
    '''Выигрышные комбинации'''
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[i][j])
            if symbols == ["X", "X", "X"]:
                print("Выиграл X!!!")
                return True
            elif symbols == ["0", "0", "0"]:
                print("Выиграл 0!!!")
                return True
    # проверка столбцов
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[j][i])
            if symbols == ["X", "X", "X"]:
                print("Выиграл X!!!")
                return True
            elif symbols == ["0", "0", "0"]:
                print("Выиграл 0!!!")
                return True

    # проверка диагонали
    symbols = []
    for i in range(3):
        symbols.append(field[i][i])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        elif symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True

    # проверка другой диагонали
    symbols = []
    for i in range(3):
        symbols.append(field[i][2-i])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        elif symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False

def player():
    '''Определение хода игрока, запуск игрового поля, проверка ввода и выигрыша'''
    num =0
    while True:
        num += 1

        show()

        if num % 2 == 0:
            print(" Ходит нолик ")
        else:
            print(" Ходит крестик ")

        # забираем координаты и проверяем условия фукцией
        x,y = ask()

        if num % 2 == 1:
            field[x][y] = "X"
        else:
            field[x][y] = "0"

        if winning_combination():
            break
        if num == 9:
            print("Ничья!")
            break

player()
