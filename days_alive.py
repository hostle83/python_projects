"""
Given two dates (date1 and date2),
computes the number of days that have passed since date1 up until date2.
"""

def isLeapYear(year):
    """
    Algorithm that determines if a given year is a leap year
    """
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


def daysInMonth(year, month):
    """
    Returns the number of days in a given month (1-12)
    """
    assert month < 13
    if month == 2:
        if isLeapYear(year):
            return 29
        return 28
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    return 30
        

def nextDay(year, month, day):
    """
    Mechanical way of advancing to the next day from a given date
    """
    assert day <= daysInMonth(year, month)
    if day < daysInMonth(year, month):
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


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    counter = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay (year1, month1, day1)
        counter = counter + 1
    return counter
