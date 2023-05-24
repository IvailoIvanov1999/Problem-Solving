int_1 = int(input())
int_2 = int(input())
int_3 = int(input())


def sum_numbers(one,two):
    sum_num = int_1 + int_2
    return sum_num


def substract(sum_num,three):
    total_num = (sum_num - int_3)
    return total_num

print(substract(sum_numbers(int_1,int_2),int_3))