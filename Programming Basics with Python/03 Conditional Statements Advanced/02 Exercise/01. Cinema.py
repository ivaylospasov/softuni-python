movie_screening = input().lower()
rows = int(input())
columns = int(input())

cinema_capacity = rows * columns

if movie_screening == 'premiere':
    income = cinema_capacity * 12.00
elif movie_screening == 'normal':
    income = cinema_capacity * 7.5
elif movie_screening == 'discount':
    income = cinema_capacity * 5.00

print(f'{income:.2f} leva')
