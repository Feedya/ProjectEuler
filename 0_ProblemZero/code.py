def calculate_sum_odd_squares(limit):
    total_sum = 0
    
    for n in range(1, limit + 1, 1):
        if (n % 2 == 1):
            total_sum += n**2
    #for n in range(1, limit + 1, 2):
    #   total_sum += n**2

    return total_sum

def main():
    limit = 895000
    
    print(f"Calcul de la somme des carrés impairs pour les {limit} premiers carrés...")
    
    result = calculate_sum_odd_squares(limit)
    
    print(f"Le résultat est : {result:,}")

if __name__ == "__main__":
    main()