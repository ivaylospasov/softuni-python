actor_name = input()
academy_points = float(input())
jury_members = int(input())

total_points = academy_points

for i in range(1, jury_members + 1):
    judge_name = input()
    judge_points = float(input())
    judge_name_length = len(judge_name)
    total_points = total_points + (judge_name_length * judge_points) / 2
    if total_points > 1250.5:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')
        break

diff_points = abs(1250.5 - total_points)

if total_points <= 1250.5:
    print(f'Sorry, {actor_name} you need {diff_points:.1f} more!')