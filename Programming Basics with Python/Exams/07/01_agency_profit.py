agency_name = input()
regular_tickets_count = int(input())
kids_tickets_count = int(input())
regular_ticket_price = float(input())
taxes = float(input())

regular_ticket_price_with_taxes = regular_ticket_price + taxes
kids_ticket_price = regular_ticket_price * (1 - 0.7)
kids_ticket_price_with_taxes = kids_ticket_price + taxes

total_sum = regular_tickets_count * regular_ticket_price_with_taxes + \
    kids_tickets_count * kids_ticket_price_with_taxes

total_profit = total_sum * 0.2

print(f'The profit of your agency from {agency_name} tickets is {total_profit:.2f} lv.')