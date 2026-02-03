import math

def write_power_digit_sum(base, exposant):
    result = base ** exposant
    print(f"result of power : {result}")
    str_result = str(result)
    liste_chiffre = [int (chiffre)for chiffre in str_result]
    sum_of_all = 0
    sum_of_all = sum(liste_chiffre)
    return (sum_of_all)

def main():
    result = write_power_digit_sum(2, 1000)
    print(f"result : {result}")

if __name__ == "__main__":
    main()