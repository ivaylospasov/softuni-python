class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        
        # Increment the total animal count only if the species is valid
        if species in ["mammal", "fish", "bird"]:
            Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result = f"Mammals in {self.name}: {', '.join(self.mammals)}"
        elif species == "fish":
            result = f"Fishes in {self.name}: {', '.join(self.fishes)}"
        elif species == "bird":
            result = f"Birds in {self.name}: {', '.join(self.birds)}"
        else:
            result = f"Invalid species: {species}"
        
        result += f"\nTotal animals: {Zoo.__animals}"
        return result


# Main program
zoo_name = input()
zoo = Zoo(zoo_name)

n = int(input())

for _ in range(n):
    animal_info = input().split()
    if len(animal_info) >= 2:
        species = animal_info[0]
        name = animal_info[1]
        zoo.add_animal(species, name)

species = input()
print(zoo.get_info(species))