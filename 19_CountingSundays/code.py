import math

#compter entre 1 janvier 1901
#jusqu a 31 december 2000
#on doit compter combien d annee on commencer par un dimanche

#une anne compte 365 jours et une annee bissextile compte 366 
# ce jour se rajoute au mois de fevrier qui va faire 29 et pas 28

#une annee est bisessextile si elle est divisible par 4 sauf 
#MAIS elle le siecle se finit par 00
#MAIS si elle se finit par 00 ET est divisible par 400 c est une annee bissextile

#1	Janvier	31
#2	Février	28 (ou 29 lors des années bissextiles)
#3	Mars	31
#4	Avril	30
#5	Mai	    31
#6	Juin	30
#7	Juillet	31
#8	Août	31
#9	Septembre	30
#10	Octobre	    31
#11	Novembre	30
#12	Décembre	31

#1 janvier 1900 etait un lundi

def put_day_in_year(year):
    if (year % 100 == 0):
        if (year % 400 == 0):
            return (366)
        return (365)
    if (year % 100 != 0 and year % 4 == 0):
        return (366)
    return (365)

def put_days_in_months(months, feb_day):
    months[0:12] = [31, feb_day, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]




def main():
    year = 1901
    day_in_year = 0
    i = 0
    counter = 0
    months_list = [0] * 12
    first_day = 2
    while (year != 2001):
        day_in_year = put_day_in_year(year)
        if (day_in_year == 365):
            put_days_in_months(months_list, 28)
        elif (day_in_year == 366):
            put_days_in_months(months_list, 29)

        i = 0
        while (i != 12):
            if (first_day == 0):
                counter += 1
            first_day = (first_day + months_list[i]) % 7
            i += 1
        
        year += 1
    print(f"result : {counter}")

if __name__ == "__main__":
    main()