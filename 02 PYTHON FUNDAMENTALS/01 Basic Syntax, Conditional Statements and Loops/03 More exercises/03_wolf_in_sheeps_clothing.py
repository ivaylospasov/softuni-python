sheep_list = input().split(", ")

sheep_list.reverse()

for index, animal in enumerate(sheep_list):
    if index == 0 and animal == "wolf":
        print("Please go away and stop eating my sheep")
        break
    elif animal == "wolf":
        print(f"Oi! Sheep number {index}! You are about to be eaten by a wolf!")
        break