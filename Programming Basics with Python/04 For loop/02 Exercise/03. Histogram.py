n = int(input())

sum_under_200 = 0
sum_bw_200_399 = 0
sum_bw_400_599 = 0
sum_bw_600_799 = 0
sum_over_800 = 0


for i in range(0, n):
    num = int(input())
    if num < 200:
        sum_under_200 += 1
    elif 200 <= num <= 399:
        sum_bw_200_399 += 1
    elif 400 <= num <= 599:
        sum_bw_400_599 += 1
    elif 600 <= num <= 799:
        sum_bw_600_799 += 1
    else:
        sum_over_800 += 1

p1 = sum_under_200 / n * 100
p2 = sum_bw_200_399 / n * 100
p3 = sum_bw_400_599 / n * 100
p4 = sum_bw_600_799 / n * 100
p5 = sum_over_800 / n * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')
