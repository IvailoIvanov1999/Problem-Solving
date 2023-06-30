from math import log

num_ber = int(input())
log_base = input()

if log_base == "natural":
    print(f"{log(num_ber):.2f}")
else:
    print(f'{log(num_ber, int(log_base)):.2f}')
