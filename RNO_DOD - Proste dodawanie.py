tab_liczb = []
tab_sum = []
suma = 0
liczba_zestawow = int(input())
for i in range(liczba_zestawow):
    suma = 0
    liczba_liczb = int(input())
    #for j in range(liczba_liczb):
    tab_liczb = input().split()
    tab_liczb = [int(x) for x in tab_liczb]
    #print(tab_liczb)
    for z in tab_liczb:
        suma = suma + z
    tab_sum.append(suma)
 
 
#tutaj za wynik będą podstawiane kolejne wartośći z tab_sum
for wynik in tab_sum:
    print(wynik)