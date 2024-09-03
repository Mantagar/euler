days = [31,28,31,30,31,30,31,31,30,31,30,31]
year = 1900
month = 0
weekday = 0

def passMonth(year, month, weekday):
    daysToPass = days[month]
    if month == 1 and year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            daysToPass += 1
    month += 1
    if month > 11:
        year += 1
        month = 0
    weekday += daysToPass
    weekday = weekday % 7
    return (year, month, weekday)

for i in range(0,12):
    year, month, weekday = passMonth(year, month, weekday)

foundSundays = 0
while year < 2001:
    if weekday == 6:
        foundSundays += 1
    year, month, weekday = passMonth(year, month, weekday)

print(foundSundays)
