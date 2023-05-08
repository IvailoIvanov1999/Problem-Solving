from collections import deque


def math_operations(*args, **kwargs):
    nums = deque(args)

    while args:
        number = nums.popleft()
        kwargs["a"] += number

        if not nums:
            break

        number = nums.popleft()
        kwargs["s"] -= number

        if not nums:
            break

        number = nums.popleft()
        if number != 0:
            kwargs["d"] /= number


        if not nums:
            break

        number = nums.popleft()
        kwargs["m"] *= number



    result = [f"{key}: {value:.1f}" for key,value in sorted(kwargs.items(), key=lambda kvpt: (-kvpt[1], kvpt[0]))]

    return "\n".join(result)

print(math_operations(6.0, a=0, s=0, d=5, m=0))
