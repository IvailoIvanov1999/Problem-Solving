def age_assignment(*args,**kwargs):
    result = []
    for names in args:
        for key,value in kwargs.items():
            if names[0] == key:
                result.append(f"{names} is {kwargs.get(key)} years old.")

    return "\n".join(sorted(result))



print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))