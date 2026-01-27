import math

def is_palindrome(nombre1, nombre2):
    result = str(nombre1 * nombre2)
    inverse = result[len(result)::-1]
    if (inverse == result):
        return (True)
    return (False)

def main():
    nombre_1 = 100
    nombre_2 = 100
    biggest = 0
    while (nombre_1 != 1000):
        nombre_2 = 100
        while (nombre_2 != 1000):
            if (is_palindrome(nombre_2, nombre_1) == True):
                if (biggest < nombre_1 * nombre_2):
                    biggest = nombre_2 * nombre_1
            nombre_2 += 1
        nombre_1 += 1
    print(f"result {biggest}")

if (__name__ == "__main__"):
    main()