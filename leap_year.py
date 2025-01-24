def leap_year_check(year):
    return year % 4 == 0 and (year % 100 !=0 or year % 400 == 0)

print(leap_year_check(2025))    