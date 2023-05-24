import datetime


e = datetime.datetime.now()

f = open("spisuk_konsumativi.txt", "a")


ustroistva_i_ceni_na_konsumativi = {

     # ustroistvo        toner kaseta cena  ,  baraban cena
      "Samsung ML-1710P":    [6.71,      0],
      "HP LaserJet P1102":   [9.45,      0],
      "Lexmark E250d":       [22.59,     39.77],
      "Ricoh MP5055SP":      [119.57,     334.74],
      "Brother HL-L2300D":     [7.65,     11.98],
      "Canon IR 2530":       [66.45,     0],
      "Canon IR 2520":       [66.45,    0],
      "HP LaserJet M1319 f": [9.67,     0],
      "HP Deskjet advantage 2515":       [8.26,     0],
      "Xerox Phaser 3020":       [13.46,     0],
      "HP LaserJet 1005":       [15.28,     0],
      "Kyocera FS1120D":       [7.91,     4.16],
      "Nashuatec Aficio MP3045":       [43.75,     0],
      "Brother DCP-7010 L":       [12.10,     23.29],
      "Brother DCP-7055":       [10.64,     15.59],
      "Brother MFC-L2740DW":       [7.85,    13.48],
      "Brother HL-2312D":       [10.67,     22.80],
      "Brother L-2512D":       [10.67,     22.80],
      "Brother L-2712DN":       [10.67,     22.80],
      "Brother DCP L5500dn":       [119.96,     4.94],
      "HP Laserjet Pro M203DN":       [9.95,     14.16],
      "Xerox B230":       [79.39,     98.50],
      "Xerox B1025 DADF":       [108.71,     29.81],

}

spisuk_s_konsumativi = ""

t = 1

while True:
    if input("Ако искате да видите списъка с устройства ,въведете ОК , или ENTER ,за да продължите .").lower() in ("ok","ок"):
        for key,value in ustroistva_i_ceni_na_konsumativi.items():
            print("От таблица N.1")
            print()
            print(f"| Устройство: {key} | Тонер цена: {value[0]:.2f} лв. | Барабан цена: {value[1]:.2f} лв. |")


    print()
    print("--------------------")
    device = input("Устройство : ")
    if device == "q" or device == "Q":
        break

    print("--------------------")

    toner_or_baraban = input("Тонер или Барабан : ").lower()

    print("--------------------")



    if device not in ustroistva_i_ceni_na_konsumativi:
        print("Няма такова устройство в списъка.")
        print("----------------------------------")


    else:
        if toner_or_baraban not in ("тонер", "toner", "барабан", "baraban"):
            print("Моля избере тонер или барабан !")
            continue

        if toner_or_baraban == "тонер" or toner_or_baraban == "toner":
            quantity = int(input("Количество тонери : "))
            print("--------------------")
            price_for_the_toner = float(ustroistva_i_ceni_na_konsumativi[device][0])
            final_price = price_for_the_toner * quantity
            print()

            print(f"Вие избрахте устройство ## {device} ## и ## ТОНЕР ## с цена за 1 бр. | {price_for_the_toner:.2f} лв. |")
            print()
            print(f"Общата сума е : | {final_price:.2f} лв. |")
            print()


            spisuk_s_konsumativi = (f"| {device} | : toneri ==> | {quantity} br. | s obshta cena ==> | {final_price:.2f} lv.|")

        elif toner_or_baraban == "baraban" or toner_or_baraban == "барабан":
            quantity = int(input("Количество барабани : "))
            print("--------------------")
            price_for_the_cartridge = float(ustroistva_i_ceni_na_konsumativi[device][1])
            final_price = price_for_the_cartridge * quantity
            print()
            print(f"Вие избрахте устройство ## {device} ## и ## БАРАБАН ## с цена за 1 бр. | {price_for_the_cartridge:.2f} лв. |")
            print()
            print(f"Общата сума е : | {final_price:.2f} лв. |")
            print()

            spisuk_s_konsumativi = (f"| {device} | : barabani ==> | {quantity} br. | s obshta cena ==> | {final_price:.2f} lv.|")


    if t == 1:
        f.write((e.strftime("                    %d-%m-%Y %H:%M:%S\n")))
        t += 1

    f.write(f"---------------------------------------------------------------\n"
        f"\n"
        f"{spisuk_s_konsumativi}\n"
        f"\n"
        f"---------------------------------------------------------------\n")




    print("--------------------------------------------------------------------")

    opit = input("Натисни | Q и enter | за изход или ENTER ,за да продължите . ").lower()

    print()

    if opit == "q":
        break
    else:
        continue

