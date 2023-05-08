def func_executor(*args):
    result = []
    for ref,par in args:
        result_func = ref(*par)
        result.append(f"{ref.__name__} - {result_func}")
    return "\n".join(result)

    # return f"{function name} - {function result}"


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result

def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))
