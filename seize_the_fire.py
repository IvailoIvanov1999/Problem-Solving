cells = input().split("#")
water = int(input())

cells_done = []
total_fire = 0

for cell in (cells):
    cell_idx = cell.split(" = ")
    level = cell_idx[0]
    value = int(cell_idx[1])

    if level == "High" and (value < 81 or value > 125):
        continue
    if level == "Medium" and (value < 51 or value > 80):
        continue
    if level == "Low" and (value < 1 or value > 50):
        continue
    if value > water:
        continue
    water -= value
    total_fire += value
    cells_done.append(value)

print(f"Cells:")
for cell in cells_done:
    print(f" - {cell}")

effort = total_fire * 0.25

print(f"Effort: {effort:.2f}")

print(f"Total Fire: {total_fire}")
