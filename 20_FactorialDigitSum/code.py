import math

def count_sum_of_power(number):
    power_result = math.factorial(100)
    print(f"{power_result}")
    string_result = str(power_result)

    liste_nombre = [int(chiffre) for chiffre in string_result]
    result = 0
    for i in liste_nombre:
        result += i
    return result

def main():
    result = count_sum_of_power(3628800)
    print(f"{result}")
    
    
if (__name__ == "__main__"):
    main()