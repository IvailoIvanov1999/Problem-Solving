length_aq = int(input())
width_aq = int(input())
high_aq = int(input())
percent = float(input())

capacity = (length_aq * width_aq * high_aq) * 0.001

percentage_taken = capacity * (percent / 100)

total=capacity-percentage_taken

print(total)
