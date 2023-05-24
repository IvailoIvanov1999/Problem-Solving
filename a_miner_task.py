word = input()
miner_taskk = {}
counter_lines = 1
while word != "stop":
    # if odd counter lines

    if counter_lines % 2 != 0:
        key = word

        if key not in miner_taskk:
            miner_taskk[key] = 0
    else:
        miner_taskk[key] += int(word)

# for el in miner_taskk:
#
#     if el in miner_taskk:
#         miner_taskk[el] += word


    counter_lines += 1
    word = input()
for el in miner_taskk:

    print(f"{el} -> {miner_taskk[el]}")

