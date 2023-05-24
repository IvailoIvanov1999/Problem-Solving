def pass_validator(pas):
    return 6<=len(pas)<=10
    # return


def contains_num_aplha(pas):
    return pas.isalnum()



def contain_2_digits_atleast(pas):
    counter = 0
    for ch in pas:
        if ch.isdigit():
            counter += 1

    return counter >= 2


password = input()
flag = True

if not pass_validator(password):
    flag = False
    print("Password must be between 6 and 10 characters")
if not contains_num_aplha(password):
    flag = False
    print("Password must consist only of letters and digits")
if not contain_2_digits_atleast(password):
    flag = False
    print("Password must have at least 2 digits")

if flag:
    print('Password is valid')
