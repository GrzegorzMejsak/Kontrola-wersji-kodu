a=int(input("Podaj przekroczenie prędkości"))
if a<=10:
    print("100 zł mandatu")
if a>=11 and a<=30:
    print("200 zł mandatu")
if a>30:
    print("400zł mandatu")