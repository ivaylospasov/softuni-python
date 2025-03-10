place_width = int(input())
place_length = int(input())
place_height = int(input())
place_volume_left = place_width * place_length * place_height

while place_volume_left > 0:
    added_boxes = input()
    if added_boxes == "Done":
        break
    else:
        added_boxes = int(added_boxes)

    if added_boxes >= place_volume_left:
        print(f"No more free space! You need {added_boxes - place_volume_left} Cubic meters more.")

    place_volume_left -= added_boxes

if place_volume_left > 0:
    print(f"{place_volume_left} Cubic meters left.")