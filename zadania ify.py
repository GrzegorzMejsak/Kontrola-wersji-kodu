a=int(input("Podaj wzrost"))

c=float(input("Podaj wagę"))
wzrost_m=a/100
b=c/(wzrost_m**2)
if a < 100:
    print("Bardzo niski wzrost")
elif a >= 100 and a < 130:
    print("Niski wzrost")
elif a >= 130 and a < 160:
    print("Normalny wzrost")
elif a >= 160 and a < 180:
    print("Jesteś wysoki")
elif a >= 180 and a<230:
    print("Jesteś ponad przeciętnie wysoki")
else:
    print("Error")
if b < 16:
    print("Jesteś wygłodzony")
elif b >= 16 and b <= 16.99:
    print("Jesteś wychudzony")

elif b >= 17 and b <= 18.49:
    print("Masz niedowagę")
elif b >= 18.5 and b <= 24.99:
    print("Twoja masa ciała jest prawidłowa")
elif b >= 25 and b <= 29.99:
    print("Masz nadwagę")
elif b >= 30 and b <= 34.99:
    print("Masz otyłość I stopnia")
elif b >= 35 and b <= 39.99:
    print("Masz otyłość II stopnia")
elif b >=40:
    print("Masz otyłość III stopnia")
else:
    print("Error")
BMI=c/(wzrost_m**2)
print("Twoje BMI wynosi:",round(BMI, 2))
granica_wyglodzenia=16*(wzrost_m**2)
granica_wychudzenia_poczatkowa=16*(wzrost_m**2)
granica_wychudzenia_koncowa=16.99*(wzrost_m**2)
granica_niedowagi_poczatkowa=17*(wzrost_m**2)
granica_niedowagi_koncowa=18.49*(wzrost_m**2)
granica_normy_poczatkowa=18.5*(wzrost_m**2)
granica_normy_koncowa=24.99*(wzrost_m**2)
granica_poczatkowa_nadwagi=25*(wzrost_m**2)
granica_koncowa_nadwagi=29.99*(wzrost_m**2)
granica_poczatkowa_otylosci_1_stopnia=30*(wzrost_m**2)
granica_koncowa_otylosci_1_stopnia=34.99*(wzrost_m**2)
granica_poczatkowa_otylosci_2_stopnia=35*(wzrost_m**2)
granica_koncowa_otylosci_2_stopnia=39.99*(wzrost_m**2)
granica_otylosci_3_stopnia=40*(wzrost_m**2)
print("Na wychudzenie waga dla Twojego wzrostu to: od", round(granica_wychudzenia_poczatkowa, 1), "do", round(granica_wychudzenia_koncowa, 1), "kg")
print("Na niedowagę waga dla Twojego wzrostu to: od", round(granica_niedowagi_poczatkowa, 1), "do", round(granica_niedowagi_koncowa, 1), "kg")
print("Na normę waga dla Twojego wzrostu to: od", round(granica_normy_poczatkowa,1), "do", round(granica_normy_koncowa, 1), "kg")
print("Na nadwagę waga dla Twojego wzrostu to: od" , round(granica_poczatkowa_nadwagi,), "do", round(granica_koncowa_nadwagi,) ,"kg")
print("Na otyłość I stopnia waga dla Twojego wzrostu to od", round(granica_poczatkowa_otylosci_1_stopnia, 1), "do", round(granica_koncowa_otylosci_1_stopnia, 1), "kg")
print("Na otyłość II stopnia waga dla Twojego wzrostu to od", round(granica_poczatkowa_otylosci_2_stopnia, 1), "do", round(granica_koncowa_otylosci_2_stopnia, 1), "kg")
print("Na otyłość III stopnia waga dla Twojego wzrostu to od", round(granica_otylosci_3_stopnia, 1), "kg")