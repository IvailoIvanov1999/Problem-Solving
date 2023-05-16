mackerel = float(input())
sprinkle = float(input())

bonito = float(input())
safrite = float(input())
mussels = int(input())

mussels_price = mussels * 7.50
# cena na palamud

bonito_price = mackerel + (mackerel * 0.60)
bonito_total = bonito * bonito_price

# cena na safrit

safrite_price = sprinkle + (sprinkle * 0.80)
safrite_total = safrite_price * safrite

all_price = safrite_total + bonito_total + mussels_price

print(f'{all_price:.2f}')
