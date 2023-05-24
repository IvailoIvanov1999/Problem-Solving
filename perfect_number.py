def perfect_number(one_num):
    divisors_sum = 0
    perfect = 0
    for num in range(1, number + 1):
        if number % num == 0:
            divisors_sum += num
    if divisors_sum // 2 == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number = int(input())

perfect_number(number)
