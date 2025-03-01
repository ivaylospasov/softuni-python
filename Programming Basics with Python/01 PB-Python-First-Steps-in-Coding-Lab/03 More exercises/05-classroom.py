hall_width = float(input())
hall_height = float(input())

corridor_width = hall_width
corridor_height = 1

workplace_width = 120
workplace_height = 70

unusable_workplace_areas = 3

# Create function for converting meters to centimeters
def convert_to_cm(dimension):
    dimension = dimension * 100
    return dimension

# Convert all dimensions to centimeters15

hall_width = convert_to_cm(hall_width)
hall_height = convert_to_cm(hall_height)
corridor_width = convert_to_cm(corridor_width)
corridor_height = convert_to_cm(corridor_height)
usable_height = hall_height - corridor_height

workplaces_on_width = hall_width // workplace_width
workplaces_on_height = usable_height // workplace_height

total_workplaces = (workplaces_on_width * workplaces_on_height) - unusable_workplace_areas

print(total_workplaces)