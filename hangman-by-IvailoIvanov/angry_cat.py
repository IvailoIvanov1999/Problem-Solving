price_rating = [int(x) for x in input().split(", ")]

entry_point = int(input())
typo_of_items = input()


left_side = price_rating[:entry_point]
right_side = price_rating[entry_point + 1:]
value = price_rating[entry_point]

if typo_of_items == "cheap":
    left = [x for x in left_side if x < value]
    right = [x for x in right_side if x < value]

else:
    left = [x for x in left_side if x >= value]
    right = [x for x in right_side if x >= value]

if sum(left) >= sum(right):
    print(f"Left - {sum(left)}")
else:
    print(f"Right - {sum(right)}")