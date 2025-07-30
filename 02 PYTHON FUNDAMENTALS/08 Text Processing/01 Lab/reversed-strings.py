text = input()

while text != "end":
    text = input()

    text_reversed = ""

    for char in reversed(text):
        text_reversed += char

print(text + " = " + text_reversed)