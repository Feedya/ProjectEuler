import math

def is_prime(nombre):
    if (nombre < 2):
        return (False)
    if (nombre == 2):
        return (True)
    if (nombre % 2 == 0):
        return (False)
    
    limite = int(math.sqrt(nombre))
    i = 2

    for i in range(3, limite + 1, 2):
        if (nombre % i == 0):
            return (False)
    return True


def main():
    nombre = 600851475143
    i = 0
    limit = int(math.sqrt(nombre))
    while (i != limit + 1):
        if (is_prime(i) and nombre % i == 0):
            print(f"result : {i}")
        i += 1    

if (__name__ == "__main__"):
    main()