import math

def see_if_divided(nombre, divisor):
    carrer = int(math.sqrt(nombre))
    counter = 0
    for i in range(1, carrer + 1, 1):
        if (nombre % i == 0):
            if (i * i == nombre):
                counter += 1
            else:
                counter += 2
    if (counter >= divisor):
        print(f"counter : {counter}")
        return (True)
    return (False)
    

def triangle_numbers_divided(divisor):
    counter = 0
    nombre = 0
    while (1):
        if (see_if_divided(nombre, divisor) == True):
            return (nombre)
        nombre += counter
        counter += 1
    return (-1)

def main():
    result = triangle_numbers_divided(500)
    print(f"result : {result}")

if __name__ == "__main__":
    main()