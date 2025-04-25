my_number = int(input())

for i in range(1111, 10000):
    a1, a2, a3, a4 = str(i)
    if int(a1) !=0 and int(a2) !=0 and int(a3) !=0 and int(a4) !=0:
        if my_number % int(a1) == 0 and my_number % int(a2) == 0 and my_number % int(a3) == 0 and my_number % int(a4) == 0:
            print(f'{a1}{a2}{a3}{a4}', end=' ')