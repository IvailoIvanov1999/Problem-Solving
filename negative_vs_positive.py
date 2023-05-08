def negative(*args):
    negatives = []
    result = 0
    for el in args:
        for item in el:
            if item < 0:
                negatives.append(item)

    result = sum(negatives)
    return result


def positive(*args):
    positives = []
    result = 0
    for el in args:
        for item in el:
            if item >= 0:
                positives.append(item)
    result = sum(positives)
    return result


def strongest(p,n):
    result = ""
    if abs(p) > abs(n):
        result = "The positives are stronger than the negatives"
    else:
        result = "The negatives are stronger than the positives"

    return result


num_s = [int(x) for x in input().split()]

print(negative(num_s))
print(positive(num_s))
print(strongest(positive(num_s),negative(num_s)))


