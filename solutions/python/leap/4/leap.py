"""Function to check leap year"""

def leap_year(year):
    """To check leap year or not"""
    if year % 400 == 0:
        return True
    if year%4 == 0 and year%100 !=0:
        return True
    return False