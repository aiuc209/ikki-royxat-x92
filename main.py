def hisobla(asos, daraja):
    natija = []
    for a, d in zip(asos, daraja):
        natija.append(a ** d)
    return natija

asos = [2, 3, 4]
daraja = [1, 2, 3]
print(hisobla(asos, daraja))
