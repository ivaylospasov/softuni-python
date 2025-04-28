movie_budget = float(input())
movie_destination = input().lower()
season = input().lower()
days_count = int(input())

movie_total_cost = 0

if movie_destination == 'dubai':
    if season == 'winter':
        movie_total_cost = 45000 * days_count * 0.7
    elif season == 'summer':
        movie_total_cost = 40000 * days_count * 0.7
elif movie_destination == 'sofia':
    if season == 'winter':
        movie_total_cost = 17000 * days_count * 1.25
    elif season == 'summer':
        movie_total_cost = 12500 * days_count * 1.25
else:
    if season == 'winter':
        movie_total_cost = 24000 * days_count
    elif season == 'summer':
        movie_total_cost = 20250 * days_count

money_difference = abs(movie_budget - movie_total_cost)

if movie_total_cost <= movie_budget:
    print(f'The budget for the movie is enough! We have {money_difference:.2f} leva left!')
else:
    print(f'The director needs {money_difference:.2f} leva more!')