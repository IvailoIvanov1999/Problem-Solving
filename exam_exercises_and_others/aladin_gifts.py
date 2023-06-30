from collections import deque


def check(s, d):
    if 100 <= s <= 199:
        d["Gemstone"] += 1

    elif 200 <= s <= 299:
        d["Porcelain Sculpture"] += 1

    elif 300 <= s <= 399:
        d["Gold"] += 1

    elif 400 <= s <= 499:
        d["Diamond Jewellery"] += 1
    return d


materials = [int(x) for x in input().split()]
magic_level_deq = deque([int(x) for x in input().split()])

gifts_dict = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0
}

while True:
    if not materials:
        break

    if not magic_level_deq:
        break

    last_material = materials.pop()
    first_magic_level = magic_level_deq.popleft()

    the_sum = last_material + first_magic_level

    check(the_sum, gifts_dict)

    if the_sum < 100:
        if the_sum % 2 == 0:
            last_material *= 2
            first_magic_level *= 3
            the_sum = last_material + first_magic_level
            check(the_sum,gifts_dict)
        else:
            the_sum *= 2
            check(the_sum, gifts_dict)

    elif the_sum > 499:
        the_sum /= 2
        check(the_sum, gifts_dict)

pair_ = False

if gifts_dict["Gemstone"] >= 1 and gifts_dict["Porcelain Sculpture"] >= 1:
    pair_ = True
elif gifts_dict["Gold"] >= 1 and gifts_dict["Diamond Jewellery"] >= 1:
    pair_ = True

if pair_:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")

if magic_level_deq:
    print(f"Magic left: {', '.join([str(x) for x in magic_level_deq])}")

sorted_output = sorted(gifts_dict.items(), key=lambda kvpt: kvpt[0])

output_text = ''

for element in sorted_output:
    if element[1] >= 1:
        output_text += f"{element[0]}: {element[1]}" + '\n'

print(output_text)