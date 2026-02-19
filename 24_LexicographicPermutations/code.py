import math

#9! = 362 880
#n = 9
#n! / (n - 1)! = premier chiffre
#n = n! 
#

def main():
    initial = 999999
    result = 0
    facto = 0
    nombre = 9
    c = 0
    all_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    while (c != 9):
        result = result * 10
        facto = math.factorial(nombre)
        index = initial // facto
        result += all_numbers.pop(index)
        initial = initial % facto
        nombre -= 1
        c += 1
    result *= 10
    print(f"result : {result}")
    return (0)
    
if __name__  == "__main__":
    main()