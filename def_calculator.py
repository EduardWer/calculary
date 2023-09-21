import math

print("Здесь вы можете посчитать всё что душе угодно")
print("Для работы вы можете использовать действия \n "
      "+ - сложение \n"
      " - - вычетание \n"
      " * - умножение \n"
      " / - деление  \n"
      " degree - степень \n"
      " root - квадратный корень числа \n"
      " facto - факториал \n"
      " sin - синус \n"
      " cos - косинус\n"
      "tan - тангенс")
print("Вычесления sin и cos - в РАДИАНАХ")

def sum(first_num):
    second_num = input("Введите следующее число >> ")
    if second_num.isnumeric():
        second_num = float(second_num)
        print(first_num + second_num)
    else:
        print("Вы ввели букву!")

def min(first_num):
    second_num = input("Введите следующее число >> ")
    if isinstance(float(second_num), (int, float)):
        second_num = float(second_num)
        print(first_num - second_num)
    else:
        print("Вы ввели букву!")


def degree():
    step = input("Введите в какую степень нужно возвести число >> ")
    if isinstance(float(step), (int, float)):
        step = int(step)
        print(pow(first_num, step))
    else:
        print("Вы ввели неправильное значение!")


def sin():
    print(f"Синус в радианах введёного числа равен {math.sin(first_num)}")

def facto(first_num):
    first_num = int(first_num)
    if first_num < 0:
        print("Факториал отрицательного числа не существует")
    else:
        print(f"Факториал введёного числа равен {math.factorial(first_num)}")


def tan():
    print(f"Тангенс в радианах введёного числа равен {math.tan(first_num)}")
def cos():
    print(f"Косинус в радианах введёного числа равен {math.cos(first_num)}")
def root():
    if first_num < 0:
        print("Корень из отрицательного числа не существует")
    else:
        print(f"Квадратный корень введёного числа равен {math.sqrt(first_num)}")
def dell():
    second_num = input("Введите следующее число >> ")
    if isinstance(float(second_num), (int, float)):
        second_num = float(second_num)
        if second_num == 0:
            print("Делить на ноль нельзя!")
        else:
            print(first_num / second_num)
    else:
        print("Вы ввели букву!")
def ym(first_num):
    second_num = input("Введите следующее число >> ")
    if isinstance(float(second_num), (int, float)):
        second_num = float(second_num)
        print(first_num * second_num)
    else:
        print("Вы ввели букву!")

while True:
    first_num = input("Введите первое число >> ")
    try:
        first_num = float(first_num)
    except ValueError:
        print("Введите число")
        continue

    action = input("Введите действие >> ")
    action = action.lower()

    match action:
        case "+":
            sum(first_num)
        case "-":
            min(first_num)
        case "*":
            ym(first_num)
        case "/":
             dell()
        case "degree":
             degree()
        case "root":
            root()
        case "facto":
            facto(first_num)
        case "sin":
            sin()
        case "cos":
            cos()
        case "tan":
            tan()
        case _:
            print("Вы где-то ошиблись, проверьте правильность ввода!")
