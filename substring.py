f_str = input()
s_str = input()

while f_str in s_str:
    s_str = s_str.replace(f_str,"")

print(s_str)