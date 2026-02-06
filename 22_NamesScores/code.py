import math
import sys #systeme


#premierement il faut les trier dans  l ordre alphabetique
#Score = Valeur du nom × Position dans la liste

def read_file(file_name):
    try:
        with open(file_name, "r") as fd:
            str_file = fd.read()
    except FileNotFoundError:
        print("On a pas reussis a ouvrir le fichier")
        sys.exit (1)
    except Exception as bizzare:
        print("erreur bizzare")
        print(f"{bizzare}")
        sys.exit (1)
    return (str_file)

def create_list(file):
    file = file.replace('"', '')
    liste_des_noms = file.split(',')
    return (liste_des_noms)    

#renvoie 1 si name1 est plus petit que name2
#renvoie -1 si name2 est plus petite que name1
def compare_names(name1, name2):
    i = 0
    while (i != len(name1) and i != len(name2)):
        if (name1[i] < name2[i]):
            return (1)
        elif (name1[i] > name2[i]):
            return (-1)
        if (name1[i] == name2[i]):
            i += 1
    if (i == len(name1) and i != len(name2)):
        return (1)
    elif (i == len(name2) and i != len(name1)):
        return (-1)
    return (0)

def put_in_alpha_order(name_list):
    i = 0
    c = 0
    while (i != len(name_list) - 1):
        c = i + 1
        if (compare_names(name_list[i], name_list[c]) == -1):
            name_list[i], name_list[c] = name_list[c], name_list[i]
            if (i != 0):
                i = i - 1
            else:
                i = 0
        else:
            i += 1
        
def count_alpha(name):
    i = 0
    result = 0
    while (i != len(name)):
        if (name[i] <= 'Z' and name[i] >= 'A'):
            result += ord(name[i]) - 64
        elif (name[i] <= 'z' and name[i] >= 'a'):
            result += ord(name[i]) - 96
        i += 1
    return (result)

def count_sum_of_all_names(liste_name):
    i = 0
    sum = 0
    result = 0
    while (i != len(liste_name)):
        alpha_somme = count_alpha(liste_name[i])
        result += alpha_somme * (i + 1)
        i += 1
    return result

def main():
    string = read_file("names.txt")
    liste_nom = create_list(string)
    put_in_alpha_order(liste_nom)
    result = count_sum_of_all_names(liste_nom)
    print(f"result : {result}")
    
if __name__ == "__main__":
    main()