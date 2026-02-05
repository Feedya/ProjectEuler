import math

def count_all_divisor(nombre):
    i = 1
    somme = 0
    while (i != nombre):
        if (nombre % i == 0):
            somme += i
        i += 1
    return somme

def count_sum_of_all_amicable_numbers(limite):
    a = 2
    b = 0
    result = 0
    while (a != 10000):
        b = count_all_divisor(a)
        if (a != b and count_all_divisor(b) == a):
            result += a
        a += 1
    return (result)


def main():
    result = count_sum_of_all_amicable_numbers(10000)
    print(f"result : {result}")

if __name__ == "__main__":
    main()