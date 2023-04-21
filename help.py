import re

n = int(input())
pattern = r"^(\$|\%)([A-Z][a-z]{2,})\1: \[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$"


for _ in range(n):
    message = input()

    match = re.findall(pattern, message)

    if not match:
        print("Valid message not found!")
    else:
        match.remove(0)


