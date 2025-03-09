goal = 10000
total_steps = 0

while total_steps < goal:
    steps = input()

    if steps != "Going home":
        steps = int(steps)
        total_steps += steps
    else:
        steps = int(input())
        total_steps += steps
        break

steps_diff = total_steps - goal

if steps_diff >= 0:
    print('Goal reached! Good job!')
    print(f'{steps_diff} steps over the goal!')
else:
    print(f'{abs(steps_diff)} more steps to reach goal.')