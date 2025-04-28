total_tickets = 0
total_students_tickets = 0
total_standard_tickets = 0
total_kids_tickets = 0
all_movies_tickets = 0


while True:
    movie_title = input()
    if movie_title == 'Finish':
        break
    free_seats = int(input())

    for seat in range(1, free_seats + 1):
        ticket_type = input()
        if ticket_type == 'End':
            break
        elif ticket_type == 'student':
            total_students_tickets += 1
        elif ticket_type == 'standard':
            total_standard_tickets += 1
        else:
            total_kids_tickets += 1
        total_tickets += 1

    print(f'{movie_title} - {(total_tickets / free_seats) * 100:.2f}% full.')

    all_movies_tickets = total_students_tickets + total_standard_tickets + total_kids_tickets
    total_tickets = 0

print(f'Total tickets: {all_movies_tickets}')
print(f'{total_students_tickets / all_movies_tickets * 100:.2f}% student tickets.')
print(f'{total_standard_tickets / all_movies_tickets * 100:.2f}% standard tickets.')
print(f'{total_kids_tickets / all_movies_tickets * 100:.2f}% kids tickets.')