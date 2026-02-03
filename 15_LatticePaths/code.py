import math

#on va utiliser le coefficiant binominal
#
#      n!
#--------------
# k! x (n - k)!
#
#n = c est le tout le nombre de pas qu on devra faire donc 40
#k = c est le nombre d elements qu on devrai choisir

def calculate_all_paths(N, K):
    if (N <= 0 or K <= 0):
        print("Not good numbers")
    N_facto = math.factorial(N)
    K_facto = math.factorial(K)
    N_minus_K_facto = math.factorial(N - K)
    result = N_facto/(K_facto * N_minus_K_facto)
    return (result)

def main():
    result = calculate_all_paths(40, 20)
    print(f"result : {result}")

if (__name__ == "__main__"):
    main()