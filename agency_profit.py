aviocompany = input()
tickets_for_adults_quantity = int(input())
childrens_tickets_quantity = int(input())
netna_price_for_ticket_for_adult = float(input())
price_for_servizing = float(input())

# code
price_for_children_ticket = netna_price_for_ticket_for_adult - (netna_price_for_ticket_for_adult * (70 / 100))
price_for_children_ticket += price_for_servizing
netna_price_for_ticket_for_adult += price_for_servizing

all_price_adults = tickets_for_adults_quantity * netna_price_for_ticket_for_adult

all_price_childrens = childrens_tickets_quantity * price_for_children_ticket

total = all_price_childrens + all_price_adults

final_price= total*(20/100)

print(f"The profit of your agency from {aviocompany} tickets is {final_price:.2f} lv.")
