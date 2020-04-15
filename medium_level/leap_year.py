########################################################################################################################
# Task
# You are given the year, and you have to write a function to check if the year is leap or not.
########################################################################################################################

def is_leap(year):
    leap = False

    if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
        leap = True
    else:
        leap = False

    return leap


year = int(input())
print(is_leap(year))
