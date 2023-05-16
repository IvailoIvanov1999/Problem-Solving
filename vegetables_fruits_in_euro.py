vegetables = float(input())

fruits = float(input())

total_kg_vegetables = int(input())

total_kg_fruits = int(input())

vegetables_cost = vegetables * total_kg_vegetables

fruit_cost = fruits * total_kg_fruits

all=fruit_cost+vegetables_cost

all_price = all / 1.94

print(f'{all_price:.2f}')
