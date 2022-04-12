#lex_auth_012693797166096384149
def find_leap_years(given_year):

    # Write your logic here
    year=0
    if(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
            year = given_year
            year = year +4
            
    else:
        year = 4- given_year%100
        year = given_year+ year +4

        
    list_of_leap_years =[]
    for i in range(15):
        
        list_of_leap_years.append(year)
        year=year+4
        
    return list_of_leap_years

list_of_leap_years= find_leap_years(1000)
print(list_of_leap_years)