num = input("Give me the number: ")

num = float(num)

if num % 1 == 0:
    print(int(num))
else:
    print(int(num) + 1)