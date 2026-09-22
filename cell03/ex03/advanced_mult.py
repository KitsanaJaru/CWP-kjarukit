num = 0
x = 0

while num <= 10:
    print(f"Table de {num}:",end=" ")
    while x <= 10:
        print(f"{num * x}",end=" ")
        x += 1
    print()
    num += 1
    x = 0