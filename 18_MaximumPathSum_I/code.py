import math

def read_file(file_name):
    try:
        fd = open(file_name, "r")
        file = fd.read()
    except FileNotFoundError:
        print("on a pas reussis a ouvrir le fichier")
        exit (0)
    fd.close()
    return (file)

def create_list(file):
    liste_total = []
    lignes_list = file.splitlines()
    for lignes in lignes_list:
        liste_mot = lignes.split()
        liste_nombre = []
        for mot in liste_mot:
            liste_nombre.append(int(mot))
        liste_total.append(liste_nombre)
    return (liste_total)


def find_biggest(liste, index_line, index_number):
    biggest = liste[index_line][index_number]
    second_biggest = liste[index_line][index_number + 1]
    if (biggest > second_biggest):
        return (biggest)
    return (second_biggest)
    
    
def calculate_biggest_sum_paths(liste):
    taille = len(liste)
    taille -= 1
    bottom = taille
    our_line = taille - 1
    index_number = 0
    i = 0
    while (our_line >= 0):
        index_number = 0
        i = 0
        while(i != len(liste[our_line])):
            biggest = max(liste[bottom][index_number], liste[bottom][index_number + 1])
            liste[our_line][index_number] += biggest
            index_number += 1
            i+= 1
        our_line -= 1
        bottom -= 1
    return (liste[0][0])



def main():
    file = read_file("numbers.txt")
    liste = create_list(file)    
    result = calculate_biggest_sum_paths(liste)
    print(f"result : {result}")

if __name__ == "__main__":
    main()