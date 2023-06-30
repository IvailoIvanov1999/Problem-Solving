def print_f_part(size):
    for ch in range(1,size+1):
        for num in range(1,ch+1):
            print(num,end=" ")
        print()

def print_s_part(size):
    for ch in range(size-1,0,-1):
        for num in range(1,ch+1):
            print(num,end=" ")
        print()


def draw_triangle(size):
    print_f_part(size)
    print_s_part(size)