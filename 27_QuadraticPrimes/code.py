import math

#n2 + (a x n) + b

#n commence a 0 et va a infinis
#on continue tant que ca donne des nombres premiers
#a, b -1000 / 1000

def next_prime(nombre):
    i = 2
    while (True):
        nombre += 1
        if (is_prime(nombre) == True):
            return nombre


def is_prime(number):
    i = 2
    if (number < 0):
        return False
    if (number == 0 or number == 1):
        return False
    if (number == 2):
        return True
    while (i != number):
        if (number % i == 0):
            return False
        i += 1
    return True

def count_biggest_prime_following(b, a):
    n = 0
    i = 0
    resul0t = 0
    while (True):
        result = n**2 + (a * n) + b
        if (result < 0 or is_prime(result) == False):
            break
        i += 1
        n += 1
    return i
        

def find_a_b(limit):
    b = 2
    result = 0
    a = -999
    biggest = 0
    while (True):
        if (b >= 1000):
            break
        a = -999
        while (a != 1000):
            following = count_biggest_prime_following(b, a)
            if (following > biggest):
                biggest = following
                result = a * b
            a += 1
        b = next_prime(b)
    return result

def main():
    result = find_a_b(1000)
    print(f"result : {result}")
    
if __name__ == "__main__":
    main()