
def all_multiples(nombre_one, nombre_two, limit):
    i = 1
    total = 0
    while (i != limit):
        if (i % nombre_one == 0 or i % nombre_two == 0):
            total += i
        i = i + 1
    return (total)

def main():
    total = 0
    total = all_multiples(5, 3, 1000)
    print(f"resultats : {total}")


if (__name__ == "__main__"):
    main()