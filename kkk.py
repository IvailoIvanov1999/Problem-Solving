figure = input()
# kvadrat,pravougulnik,trapec,romb,triugulnik pravougulen,ostrougulen triugulnik,tupougulen triugulnik,krug,usporednik,kub,cilindur,sfera
while figure == 'kvadrat' or 'квадрат' or 'Квадрат' or 'square' or 'Square' or 'Kvadrat':

    searching = input('Въведете какво търсим : ')
    if searching == 'P' or 'p' or 'perimetyr' or 'perimetur' or 'Perimetyr' or 'Perimetur' or 'obikolka' or 'Obikolka' or 'Обиколка' or 'обиколка' or 'Периметър' or 'периметър':
        side = float(input('Въведете стойност на страната (а): '))
        p = 4 * side
        print('P - обиколка ')
        print('P = 4*a')
        print(f'{p:.2f}')



    elif searching == 'lice' or searching == 'Lice' or searching == 'S' or searching == 's' or searching == 'Лице' or searching == 'лице':
        side = float(input('Въведете стойност на страната (а): '))
        s = side * side
        print('S - лице ')
        print('S = a*a ')
        print(f'{s:.2f}')

    if searching == 'stop' or searching == 'end' or searching == 'край':
        break

while figure == 'romb':
    print(figure)