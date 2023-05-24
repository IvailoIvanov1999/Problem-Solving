price_in_dollars_processors = float(input())
price_in_dollars_video_cards = float(input())
price_in_dollars_ram = float(input())

count_ram_memories = int(input())
percent_discount = float(input())

price_in_dollars_processors = price_in_dollars_processors * 1.57
price_in_dollars_video_cards = price_in_dollars_video_cards * 1.57
price_in_dollars_ram = price_in_dollars_ram * 1.57



price_in_dollars_processors = price_in_dollars_processors - (price_in_dollars_processors * (percent_discount ))

price_in_dollars_video_cards = price_in_dollars_video_cards - (price_in_dollars_video_cards * (percent_discount ))


ram_pamet_price = count_ram_memories * price_in_dollars_ram

total = ram_pamet_price + price_in_dollars_processors + price_in_dollars_video_cards

print(f'Money needed - {total:.2f} leva.')
