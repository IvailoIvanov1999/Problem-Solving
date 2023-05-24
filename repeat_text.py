text = input()
times = input()

if times.isalpha():
    print("Variable times must be an integer")
else:
    n = int(times)
    final_output = text * n
    print(final_output)
