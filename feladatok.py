def feladat_1():
    i = 0
    for i in range(0, 151, 2):
        print(i, end=" ")

def feladat_1a():
    a = int(input("Adj meg egy számot: "))
    b = int(input("Adj meg egy nagyobb számot: "))
    if a%2 ==1:
        for i in range(a+1, b+1, 2):
            print(i, end=" ")
    else:
        for i in range(a, b, 2):
            print(i, end=" ")

def feladat_3():
    szam= int(input("Adj meg egy 10-zel osztható számot!= "))
    while not (szam % 10 == 0):
        print("Hiba!")
        szam = int( input( "Adj meg egy 10-zel osztható számot!: "))

    #for i in range(szam):
        #print("*", end=" ")
    # ugyanazt csinálja, de mostantól a for-t preferáljuk...
    i = 0
    while i < szam:
        print("*", end= " ")
        i += 1

def feladat_4():
    szam = int(input("Adj meg egy kétjegyű páros számot!: "))
    while not( szam % 2 == 0 and ( 9<= szam< 100 or -99 < szam< -10)):
        print("Hiba! ")
        szam= int(input("Adj meg egy kétjegyű páros számot!: "))
    for i in range(szam):
        print("*", end=" ")