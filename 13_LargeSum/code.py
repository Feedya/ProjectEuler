import math

#[ <Action sur l'objet> for <nom_variable> in <source> if <condition> ]

def read_file(name):
    try:
        with open(name, "r") as fd:
            string = fd.read()
    except FileNotFoundError:
        print("on a pas reussis a ouvrir le fihcier")
        exit (1)
    string = string.replace("\n", " ")
    return (string)

def create_number_list(nbr_str):
    tab = [int(i) for i in nbr_str.split() if i.isdigit()]
    return tab

def sum_all(tab):
    result = 0
    for i in tab:
        result += i
    return (result)

def main():
    nombres_str = read_file("numbers.txt")
    tab = create_number_list(nombres_str)
    result = sum_all(tab)
    print(f"resultat : {str(result)[0:10]}")
    
if (__name__ == "__main__"):
    main()