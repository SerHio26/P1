
file = open("num_1.txt", "r")

num = file.readline()

for el in num:
    print(el)


file2 = open("num_2.txt", "w")

file2.write(num)

file.close()
file2.close()