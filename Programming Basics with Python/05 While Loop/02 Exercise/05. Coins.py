change_in_leva = float(input())

leva_2: int = int(0)
leva_1: int = int(0)
stotinki_50: int = int(0)
stotinki_20: int = int(0)
stotinki_10: int = int(0)
stotinki_5: int = int(0)
stotinki_2: int = int(0)
stotinki_1: int = int(0)

coins_counter: int = int(0)

change_in_stotinki: int = int(change_in_leva * 100)

if change_in_leva < 0:
    raise ValueError('The change cannot be negative')

if change_in_leva == 0:
    pass

if change_in_stotinki >= 200:
    leva_2 = int(change_in_stotinki // 200)
    coins_counter += leva_2
    change_in_stotinki = change_in_stotinki - (leva_2 * 200)

if 100 <= change_in_stotinki < 200:
    leva_1 = int(change_in_stotinki // 100)
    coins_counter += leva_1
    change_in_stotinki = change_in_stotinki - (leva_1 * 100)

if 50 <= change_in_stotinki < 100:
    stotinki_50 = int(1)
    coins_counter += stotinki_50
    change_in_stotinki = change_in_stotinki - (stotinki_50 * 50)

if 20 <= change_in_stotinki < 50:
    stotinki_20 = int(change_in_stotinki // 20)
    coins_counter += stotinki_20
    change_in_stotinki = change_in_stotinki - (stotinki_20 * 20)

if 10 <= change_in_stotinki < 20:
    stotinki_10 = int(change_in_stotinki // 10)
    coins_counter += stotinki_10
    change_in_stotinki = change_in_stotinki - (stotinki_10 * 10)

if 5 <= change_in_stotinki < 10:
    stotinki_5 = int(change_in_stotinki // 5)
    coins_counter += stotinki_5
    change_in_stotinki = change_in_stotinki - (stotinki_5 * 5)

if 2 <= change_in_stotinki < 5:
    stotinki_2 = int(change_in_stotinki // 2)
    coins_counter += stotinki_2
    change_in_stotinki = change_in_stotinki - (stotinki_2 * 2)

if 1 <= change_in_stotinki < 2:
    stotinki_1 = int(1)
    coins_counter += 1
    change_in_stotinki = change_in_stotinki - stotinki_1

print(int(coins_counter))