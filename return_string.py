word = input()
counter = int(input())

# lambda solution
repeat = lambda a, b: a * b
result = repeat(word, counter)
print(result)

# def solution

def repeat():
    gg=word * counter
    print(gg)

repeat()
