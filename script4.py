wiek = int(input("Podaj wiek: "))
odpowiedz = input("Czy ma prawo jazdy? (tak/nie): ").strip().lower()
ma_prawo_jazdy = odpowiedz == "tak"

if wiek >= 13:
    print("Możesz mieć prawo jazdy.")
    if ma_prawo_jazdy:
        print("Możesz prowadzić motorower.")
    else:
        print("Zrób najpierw prawo jazdy.")
else:
    print("Nie masz wystarczającego wieku, aby prowadzić motorower.")









