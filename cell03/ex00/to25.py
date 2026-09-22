num = int(input("Enter a number less than 25: "))

if num > 25:
    print("Enter a number less than 25.")
else:
    for i in range(num, 26):
        print("Inside the loop, my variable is now: ", i)