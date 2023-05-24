number = [int(x) for x in input().split()]


def mini_maxi_sumall():
    minimum = min(number)
    maximum = max(number)
    total_sum = sum(number)

    print(f"The minimum number is {minimum}")
    print(f"The maximum number is {maximum}")
    print(f"The sum number is: {total_sum}")


mini_maxi_sumall()
