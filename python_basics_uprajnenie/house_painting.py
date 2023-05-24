# zelena_boq_razhod_na_litur=   3.4  na kv.m
# chervena= 4.3 na kv.m


# vrata_na_prednata_stena=  1.20 x 2\

house_hight_x = float(input())

house_lenght_y = float(input())

roof_triangle_wall_h = float(input())
# predna i zadna stena
front_back_side_square_meters = (house_hight_x * house_hight_x * 2) - 2.4

# dvete stranichni steni
sided_walls_square_meters = 2 * (house_hight_x * house_lenght_y - 2.25)

# zelena_boq
totall_green_paint_ltrs = (front_back_side_square_meters + sided_walls_square_meters) / 3.4

print(f'{totall_green_paint_ltrs:.2f}')

# stranite na pokriva
roof_sides = 2 * (house_hight_x * house_lenght_y)

# dvata razvnostranni triugulnika
triangle_roof_sm = 2 * (house_hight_x * roof_triangle_wall_h / 2)

total_triangle_paint_litres = (roof_sides + triangle_roof_sm)/4.3

print(f'{total_triangle_paint_litres:.2f}')



