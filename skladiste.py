print ("1 - Unos robe,\n2 - Prikazivanje robe u skladištu,\n3 - Brisanje artikla,\n4 - Prikazivanje kompletnog stanja skladišta,\n5 - Dodavanje opisa proizvoda unutar skladišta,\n6 - Ispis svih detalja vezanih za pojedinačni proizvod,\n7 - Izlaz iz programa.")

roba = []
roba_details = []
roba_place = 1
place_name_holder = 0
place_desc_holder = 1
place_price_holder = 2

while True:
    user_input = int(input("Unesite željenu komandu: "))
    if user_input == 1:
        unesi_robu = input("Unesite naziv robe: ")
        roba.append([unesi_robu])
    if user_input == 2:
        for i in roba:
            print (roba_place, i[0])
            roba_place = roba_place + 1
        roba_place = 1
    if user_input == 3:
        for i in roba:
            print (roba_place, i[0])
            roba_place = roba_place + 1
        roba_place = 1
        user_roba_remove = int(input("Unesite broj robe koju želite obrisati: "))
        if user_roba_remove == 1:
            roba.remove(roba[0])
        if user_roba_remove == 2:
            roba.remove(roba[1])
        if user_roba_remove == 3:
            roba.remove(roba[2])
        if user_roba_remove == 4:
            roba.remove(roba[3])
    if user_input == 5:
        for j in roba:
            print (roba_place, j[0])
            roba_place = roba_place + 1
        roba_place = 1
        opis_robe = int(input("Unesite željenu robu: "))
        for k,v in enumerate(roba):
            opis_robe = opis_robe - 1
            if opis_robe == k: 
                user_details_input = input ("Unesite opis: ")
                roba[k].append(user_details_input)
                user_price_input = input ("Unesite cijenu: ")
                roba[k].append(user_price_input)
            opis_robe = opis_robe + 1
    if user_input == 4:
        print(roba)
    if user_input == 6:
        for i in roba:
            print (roba_place, i[0])
            roba_place = roba_place + 1
        roba_place = 1
        roba_demand_details = int(input("Unesite broj artikla: "))
        for k,v in enumerate(roba):
            roba_demand_details = roba_demand_details - 1
            if roba_demand_details == k:
                print(f"Naziv artikla: {roba[k][place_name_holder]},\nOpis artikla: {roba[k][place_desc_holder]},\nCijena artikla: {roba[k][place_price_holder]}")
            roba_demand_details = roba_demand_details + 1
    if user_input == 7:
        print("Ugodan ostatak dana.")
        break
    
    




        

