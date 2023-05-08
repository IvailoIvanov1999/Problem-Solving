def recursive_power(num, power):
    result = 1
    for _ in range(power):
        result *= num

    return result


print(recursive_power(10, 100))