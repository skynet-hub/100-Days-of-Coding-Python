def is_leap(year):

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False        
    
def days_in_months(year_checked, month_checked):
    if month > 12 or month < 1:
        return "Invalid input"
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    if is_leap(year_checked) and month == 2:
        return 29
    return days[month_checked - 1]    




year = int(input("Enter a year: "))     
month = int(input("Enter a month: "))
days = days_in_months(year, month)
print(days)