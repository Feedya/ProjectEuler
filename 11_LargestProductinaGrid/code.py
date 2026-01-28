import math

def read_file(name):
    try:
        fd = open(name, "r")
        string = fd.read()
        fd.close()
    except FileNotFoundError:
        print("On a pas trouver le fichier")
        exit (0)
    string = string.replace("\n", " ")
    return (string)

#ici on va utiliser split qui split une string en fonction des espaces
#mais split retourne des string et nous on veut des nombres
#donc on va donner string par string avec le for depuis le split
#et avec le int() on va transformer en nombre et le i.isdigit c est pout verifier
#comment lire
#[ <Action sur l'objet> for <nom_variable> in <source> if <condition> ]
def put_all_numbers_in_tab(texte):
    tab = [int(i) for i in texte.split() if i.isdigit()]
    return (tab)

def count_in_front(tab, i):
    four_numbers_tab = tab[i: i + 4]
    result = 1
    for i in four_numbers_tab:
        result *= i
    return (result)    
    
def count_in_back(tab, i):
    result = 1
    if (i >= 4):
        tab_of_four = tab[i : i - 4 : -1]
        for i in tab_of_four:
            result *= i
        return (result)
    return (0)
    
    
    
def count_product_in_diagonal_down_right(tab, i):
    taille = len(tab)
    result = 1
    if (i + 21 > taille):
        return (0)
    result *= tab[i]
    i += 21
    if (i + 21 > taille):
        return (0)
    result *= tab[i]
    i += 21
    if (i + 21 > taille):
        return (0)
    result *= tab[i]
    i += 21
    if (i + 21 > taille):
        return (0)
    result *= tab[i]
    return (result)
    
def count_product_in_diagonal_down_left(tab, i):
    taille = len(tab)
    result = 1
    if (i + 19 > taille):
        return (0)
    result *= tab[i]
    i += 19
    if (i + 19 > taille):
        return (0)
    result *= tab[i]
    i += 19
    if (i + 19 > taille):
        return (0)
    result *= tab[i]
    i += 19
    if (i + 19 > taille):
        return (0)
    result *= tab[i]
    return (result)

def count_product_down(tab, i):
    taille = len(tab)
    result = 1
    if (i + 20 > taille):
        return (0)
    result *= tab[i]
    i += 20
    if (i + 20 > taille):
        return (0)
    result *= tab[i]
    i += 20
    if (i + 20 > taille):
        return (0)
    result *= tab[i]
    i += 20
    if (i + 20 > taille):
        return (0)
    result *= tab[i]
    return (result)

def count_product_up(tab, i):
    taille = len(tab)
    result = 1
    if (i < 60):
        return (0)
    result *= tab[i]
    result *= tab[i - 20]
    result *= tab[i - 40]
    result *= tab[i - 60]
    return (result)

def count_product_up_right(tab, i):
    taille = len(tab)
    result = 1
    if (i < 57):
        return (0)
    result *= tab[i]
    result *= tab[i - 19]
    result *= tab[i - 38]
    result *= tab[i - 57]
    return (result)

def count_product_up_left(tab, i):
    taille = len(tab)
    result = 1
    if (i < 63):
        return (0)
    result *= tab[i]
    result *= tab[i - 21]
    result *= tab[i - 42]
    result *= tab[i - 63]
    return (result)



    
def count_product_of_all_direction(tab, i):
    biggest = 0

    biggest_front = count_in_front(tab, i)
    biggest_back = count_in_back(tab, i)

    biggest_diagonal_down_right = count_product_in_diagonal_down_right(tab, i)
    biggest_diagonal_down_left = count_product_in_diagonal_down_left(tab, i)
    biggest_down = count_product_down(tab, i)

    biggest_up = count_product_up(tab, i)
    biggest_up_right = count_product_up_right(tab, i)
    biggest_up_left = count_product_up_left(tab, i)

    biggest_of_biggest = max(biggest_front, biggest_back, biggest_diagonal_down_left, biggest_diagonal_down_right,
                             biggest_down, biggest_up, biggest_up_left, biggest_up_right)
    return (biggest_of_biggest)

def find_biggest_product(tab):
    biggest = 0
    new_biggest = 0
    index = 0
    for i in tab:
        new_biggest = count_product_of_all_direction(tab, index)
        if (new_biggest > biggest):
            biggest = new_biggest
        index += 1
    return (biggest)


def main():
    texte = read_file("numbers.txt")
    tab = put_all_numbers_in_tab(texte)
    result = find_biggest_product(tab)
    print(f"resultats : {result}")
    
if __name__ == "__main__":
    main()