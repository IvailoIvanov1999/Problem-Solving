import re

word = input()

# regex = r"\b[\.\-\_a-zA-Z0-9]+@[\.\-\_a-zA-Z0-9]+\b"
regex = r"\s([a-zA-Z0-9][.\-\w]*[a-zA-Z0-9]@[a-zA-Z][a-zA-Z\-]*[a-zA-Z](\.[a-zA-Z][a-zA-Z\-]*[a-zA-Z])+)"

regexed_word = re.findall(regex, word)

print("\n".join(groups[0] for groups in regexed_word))
