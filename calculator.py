# Инженерный колькулятор практос
import math
from art import tprint

tprint("UNAnov")

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
while True:
    first_num = input("Введите первое число >> ")
    try:
        first_num = float(first_num)
    except ValueError:(
            print("Учите числа"))

    if isinstance(first_num, (int,float)):
        #first_num = float(first_num)
        action = input("Введите действие >>")
        action = action.lower()
        match action:
            case "+":
                second_num = input("Введите следующее число>>")
                if second_num.isnumeric():
                    second_num = float(second_num)
                    print(first_num + second_num)
                else:
                    print("Вы ввели букву!!")

            case "-":
                second_num = input("Введите следующее число>>")
                if  isinstance(float(second_num), (int, float)):
                    second_num = float(second_num)
                    print(first_num - second_num)
                else:
                    print("Вы ввели букву!!")
            case "*":
                second_num = input("Введите следующее число>>")
                if  isinstance(float(second_num), (int, float)):
                    second_num = float(second_num)
                    print(first_num * second_num)
                else:
                    print("Вы ввели букву!!")
            case "/":
                second_num = input("Введите следующее число>>")
                if  isinstance(float(second_num), (int, float)):
                    second_num = float(second_num)
                    if second_num == 0:
                        print("Делить на ноль нельзя !!!")
                    else:
                        print(first_num / second_num)
                else:
                    print("Вы ввели букву!!")
            case "degree":
                step = input("Введите в какую стпень нужно возвести число>> ")
                if  isinstance(float(step), (int, float)):
                    step = int(step)
                    print(pow(first_num, step))
                else:
                    print("Вы что то неправильно ввели ")
            case "root":
                if first_num < 0:
                    print("Корень отриц. чисел не существует")
                else:
                    print(f"Квадратный корень введёного числа равен {math.sqrt(first_num)}")
            case "facto":
                first_num = int(first_num)
                if first_num <0:
                    print("Не существует")
                else:
                    print(f"Факториал введёного числа равен {math.factorial(first_num)}")
            case "sin":
                print(f"Синус в радианах  введёного числа равен {math.sin(first_num)}")
            case "cos":
                print(f"Косинус в радианах введёного числа равен {math.cos(first_num)}")
            case "tan":
                print(f"Тангенс в радианах равен {math.tan(first_num)}")
            case _:
                print("Вы где то ошиблись проверьте правильность ввода!")


    else:
        print("Вы не ввели число проверьте правильность написания!")
