first_number = input()
second_number = input()

a1, a2, a3, a4 = first_number
b1, b2, b3, b4 = second_number

for num1 in range(int(a1), int(b1) + 1):
    for num2 in range(int(a2), int(b2) + 1):
        for num3 in range(int(a3), int(b3) + 1):
            for num4 in range(int(a4), int(b4) + 1):
                if num1 % 2 != 0 and num2 % 2 != 0 and num3 % 2 != 0 and num4 % 2 != 0:
                    print(f"{num1}{num2}{num3}{num4}", end=" ")