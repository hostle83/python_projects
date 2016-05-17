# program computes the number of days a person has been alive since his/her birthday


def is_leap_year(year):
    """
    Returns true if the input year is a leap year, false otherwise
    """
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


def days_left(year, month, day):
    """
    Computes the days left in a given year starting from the input date
    """
    result = 0
    # 31 days in a month if Jan, Mar, May, July, Aug, Oct, Dec
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        # days to end of month
        result = 31 - day
    # 30 days if Apr, June, Sept, Nov
    elif month == 4 or month == 6 or month == 9 or month == 11:
        result = 30 - day
    else:
        if is_leap_year(year):
            result = 29 - day
        else:
            result = 28 - day
    # add days from remaining months
    if month % 12 != 0:
        while month < 12:
            month = month + 1
            if month == 2:
                if is_leap_year(year):
                    result = result + 29
                else:
                    result = result + 28
            elif month == 3:
                result = result + 31
            elif month == 4:
                result = result + 30
            elif month == 5:
                result = result + 31
            elif month == 6:
                result = result + 30
            elif month == 7:
                result = result + 31
            elif month == 8:
                result = result + 31
            elif month == 9:
                result = result + 30
            elif month == 10:
                result = result + 31
            elif month == 11:
                result = result + 30
            elif month == 12:
                result = result + 31
    return result


       
        
