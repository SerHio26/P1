import sys

def handler(str):
    return input(str)

def hello():
    print("Добро пожаловать!")

def bye():
    print("Досвидания!")

def exit():
    bye()
    sys.exit()

def start():
    a = handler("Введите первое число: ")
    b = handler("Введите второе число: ")
    operator = handler("Введите что вы хотите сделать? Например: +, -, /, *, %, **, //: ")
    resolver(a, b, operator)


def resolver(a, b, operator):
    print("Результат вычисления: ")
    try:
        if operator == "+":
            print(int(a) + int(b))
        elif operator == "-":
            print(int(a) - int(b))
        elif operator == "/":
            print(int(a) / int(b))
        elif operator == "*":
            print(int(a) * int(b))
        elif operator == "%":
            print(int(a) % int(b))
        elif operator == "**":
            print(int(a) ** int(b))
        elif operator == "//":
            print(int(a) // int(b))
        else:
            print("Оператор не найден")
    except Exception as error:
        print("Вычисление не удалось, попробуйте еще раз", error)

def menu():
    hello()
    while True:
        print("Приветствуем в калькуляторе!")
        operation = input("Выберите режим: go - режим калькулятора, ex - выход из программы: ")
        match operation:
            case "go":
                start()
            case "ex":
                exit()

def main():
    menu()
if __name__ == "__main__":
    main()




