

first = int(input())
second = int(input())
third = int(input())

if first == second and first == third:
    print("Совпадений: 3")
elif first == second or first == third:
    print('Совпадений: 2')
else:
    print("Совпадений нет")