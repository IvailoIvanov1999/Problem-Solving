words = input().split(" ")
palindrome_word = input()
palindromes_list =[]
counter = 0

for el in words:
    if el == palindrome_word:
        counter += 1
    if el == "".join(reversed(el)):
        palindromes_list.append(el)
print(palindromes_list)
print(f'Found palindrome {counter} times')
