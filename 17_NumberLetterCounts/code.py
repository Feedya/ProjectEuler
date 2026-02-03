import math

def count_dizaine(nombre):
    restes = nombre % 10
    dizaine = nombre - restes
    return dizaine

def mettre_en_uniter(nombre):
    uniter = nombre % 10
    return (uniter)

#on doit enlecer couche par couche
def count_longueur(nombre):
    units = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4}
    teens = {10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8}
    tens = {20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6}
    somme = 0
    in_hundrer = 0
    if (nombre == 1000):
        return (11)
    if (nombre == 100):
        return (10)
    if (nombre > 0 and nombre < 10):
        somme = units[nombre]
        return (somme)
    if (nombre > 100):
        in_hundrer = 1
        restes = nombre // 100
        somme += units[restes] + 7
        nombre = nombre - (restes * 100)
    if (nombre >= 10 and nombre < 20):
        somme += teens[nombre]
        if (in_hundrer == 1):
            somme += 3
    elif (nombre >= 20 and nombre <= 99):
        dizaine = count_dizaine(nombre)
        somme += tens[dizaine]
        if (in_hundrer == 1):
            somme += 3
        nombre = mettre_en_uniter(nombre)
        if (nombre != 0):
            in_hundrer = 2
    if (nombre > 0 and nombre < 10):
        somme += units[nombre]
        if (in_hundrer == 1):
            somme += 3
    return (somme)


def count_sum_of_letters(limite):

    somme_totale = 0
    for i in range(limite + 1):
        longueur_du_nombre = count_longueur(i)
        somme_totale = somme_totale + longueur_du_nombre
    return (somme_totale)

def main():
    result = count_sum_of_letters(1000)
    print(f"result : {result}")


if __name__ == "__main__":
    main()
    