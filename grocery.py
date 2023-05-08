def grocery_store(**kwargs):
    result = []
    sorted_receipt = sorted(kwargs.items(),key=lambda kvpt: (kvpt[1],len(kvpt[0]),sorted(kvpt[0])),reverse=True)
    for k,v in sorted_receipt:
        result.append(f"{k}: {v}")

    return "\n".join(result)

print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
