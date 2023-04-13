def is_leap_year(year):
    
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def next_day(day, month, year):
    
    days_in_month = [31, 28 + is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if day < days_in_month[month - 1]:
        return day + 1, month, year
    elif month == 12:
        return 1, 1, year + 1
    else:
        return 1, month + 1, year

day = int(input("Digite o dia: "))
month = int(input("Digite o mês: "))
year = int(input("Digite o ano: "))

next_day = next_day(day, month, year)

print(f"A data do próximo dia é: {next_day[0]}/{next_day[1]}/{next_day[2]}")
