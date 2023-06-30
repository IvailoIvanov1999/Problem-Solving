fib_ll = []
while True:
    command = input().split()
    if command[0] == "Stop":
        break

    if command[0] == "Create":
        num_ = int(command[2])
        for i in range(num_):
            if i == 0:
                fib_ll = [0]
                continue
            if i == 1:
                fib_ll = [0, 1]
                continue
            result = fib_ll[-1] + fib_ll[-2]
            fib_ll.append(result)
        print(*fib_ll)

    elif command[0] == "Locate":
        num_locate = int(command[1])
        if num_locate in fib_ll:
            print(f"The number - {num_locate} is at index {fib_ll.index(num_locate)}")
        else:
            print(f"The number {num_locate} is not in the sequence")
