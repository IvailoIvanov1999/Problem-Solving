packet_pens = 5.80
packet_markers = 7.20
cleaner = 1.20

number_of_pens = int(input())

number_of_markers = int(input())

cleaner_ltr = int(input())

percent_discount = int(input())

price_for_pens = number_of_pens * packet_pens

price_for_markers = number_of_markers * packet_markers

price_for_cleaner = cleaner_ltr * cleaner

price_for_everything = price_for_pens + price_for_markers + price_for_cleaner
discount=price_for_everything*(percent_discount/100)
total=price_for_everything-discount


print(total)
