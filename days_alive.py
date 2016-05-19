



def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

        
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """
    Returns True if year1, month1, day1 is before year2, month2, day2;
    otherwise return False
    """
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

print dateIsBefore(2012, 12,12,2012, 12, 13)


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    counter = 0
    while (year1, month1, day1) != (year2, month2, day2):
        year1, month1, day1 = nextDay (year1, month1, day1)
        counter = counter + 1
    return counter

