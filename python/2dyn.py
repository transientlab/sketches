# funkcja do obliczania masy
def obliczanie_masy(przysp, sila):
    return sila/przysp

#  funkcja do obliczania sily
def sila(przysp, masa):
    return przysp*masa

# funkcja do obliczania przyspieszenia
def przysp(sila, masa):
    return sila/masa

# oblicz mase ciala na które działa sila1 a porusza się ono z przysp1
sila1 = 5
przysp1 = 30

# oblicz sile dzialajaca na cialo o masie masa2 i przyspieszeniu przysp2
masa2 = 743345454
przysp2 = 12054353



# print( obliczanie_masy(przysp=przysp1, sila=sila1) )

print( sila(przysp2, masa2) )


