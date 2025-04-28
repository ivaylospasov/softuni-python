jury_count = int(input())
total_score = 0
average_score = 0
presentation_score = 0
presentation_count = 0

while True:
    presentation_name = input()

    if presentation_name == 'Finish':
        break
    else:
        presentation_count += 1
        for assessment in range(jury_count):
            score = float(input())
            presentation_score += score
            total_score += score

        print(f'{presentation_name} - {presentation_score / jury_count:.2f}.')
        presentation_score = 0

average_score = total_score / (presentation_count * jury_count)
print(f"Student's final assessment is {average_score:.2f}.")

