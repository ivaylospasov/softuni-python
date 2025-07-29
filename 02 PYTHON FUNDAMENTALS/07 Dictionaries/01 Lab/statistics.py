products = {}

while True:
    command = input()
    
    if command == "statistics":
        break
    
    product, quantity = command.split(": ")
    quantity = int(quantity)
    
    if product in products:
        products[product] += quantity
    else:
        products[product] = quantity

print("Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")