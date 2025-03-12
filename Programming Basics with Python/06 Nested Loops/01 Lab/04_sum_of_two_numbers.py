start = int(input())
end = int(input())
magic_number = int(input())
counter = 0

for i in range(start, end + 1):
    for j in range(start, end + 1):
        counter += 1 # count the combinations
        if i + j == magic_number: # check if the sum is equal to the magic number
            print(f"Combination N:{counter} ({i} + {j} = {magic_number})")
            break
        if i == end and j == end: # check if the magic number is not found
            print(f"{counter} combinations - neither equals {magic_number}")
            break
    if i + j == magic_number: # check if the sum is equal to the magic number
        break   # break the outer loop. If not all combinations will be checked
