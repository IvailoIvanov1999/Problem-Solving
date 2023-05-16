chicken_meal_menu = 10.35
fish_meal_menu = 12.40
vegetarian_meal_menu = 8.15
delivery = 2.50

chicken_menu = int(input())
price_chicken_menu = float(chicken_meal_menu * chicken_menu)

fish_menu = int(input())
price_fish_menu = float(fish_menu * fish_meal_menu)

vegetarian_menu = int(input())
price_vegetarian_menu = float(vegetarian_menu * vegetarian_meal_menu)

all_menu_price = float(price_vegetarian_menu + price_fish_menu + price_chicken_menu)

dessert=float(all_menu_price * 0.20)

all_price=float(all_menu_price+dessert+delivery)

print(all_price)
