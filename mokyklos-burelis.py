
bureliai = {
    "Krepsinis": {
        "vadovas": "Jonas",
        "maks": 3,
        "dalyviai": []
    },
    "Dailes": {
        "vadovas": "Ona",
        "maks": 2,
        "dalyviai": []
    },
    "Programavimas": {
        "vadovas": "Petras",
        "maks": 3,
        "dalyviai": []
    }
}

while True:
    print("\n1. Rodyti burelius")
    print("2. Priskirti mokini")
    print("3. Pasalinti mokini")
    print("4. Baigti")

    pasirinkimas = input("Pasirinkite: ")

    if pasirinkimas == "1":
        for pavadinimas in bureliai:
            print("\nPavadinimas:", pavadinimas)
            print("Vadovas:", bureliai[pavadinimas]["vadovas"])
            print("Maksimalus skaicius:", bureliai[pavadinimas]["maks"])
            print("Dalyviai:", bureliai[pavadinimas]["dalyviai"])

    elif pasirinkimas == "2":
        vardas = input("Mokinio vardas: ")

        jau_yra = False

        for pavadinimas in bureliai:
            if vardas in bureliai[pavadinimas]["dalyviai"]:
                jau_yra = True

        if jau_yra:
            print("Mokinys jau priskirtas bureliui!")
            continue

        print("Bureliai:")
        for pavadinimas in bureliai:
            print(pavadinimas)

        pasirinkimas_burelio = input(
            "Pasirinkite bureli arba spauskite Enter automatiniam priskyrimui: "
        )

        if pasirinkimas_burelio == "":
            maziausias = None

            for pavadinimas in bureliai:
                if len(bureliai[pavadinimas]["dalyviai"]) < bureliai[pavadinimas]["maks"]:
                    if maziausias == None:
                        maziausias = pavadinimas
                    elif len(bureliai[pavadinimas]["dalyviai"]) < len(bureliai[maziausias]["dalyviai"]):
                        maziausias = pavadinimas

            if maziausias == None:
                print("Visi bureliai pilni")
            else:
                bureliai[maziausias]["dalyviai"].append(vardas)
                print("Mokinys priskirtas i", maziausias)

        elif pasirinkimas_burelio in bureliai:
            if len(bureliai[pasirinkimas_burelio]["dalyviai"]) < bureliai[pasirinkimas_burelio]["maks"]:
                bureliai[pasirinkimas_burelio]["dalyviai"].append(vardas)
                print("Mokinys priskirtas")
            else:
                print("Burelis pilnas")

        else:
            print("Tokio burelio nera")

    elif pasirinkimas == "3":
        vardas = input("Koki mokini pasalinti? ")
        rasta = False

        for pavadinimas in bureliai:
            if vardas in bureliai[pavadinimas]["dalyviai"]:
                bureliai[pavadinimas]["dalyviai"].remove(vardas)
                rasta = True
                print("Mokinys pasalintas")

        if rasta == False:
            print("Mokinys nerastas")

    elif pasirinkimas == "4":
        break

    else:
        print("Neteisingas pasirinkimas")
