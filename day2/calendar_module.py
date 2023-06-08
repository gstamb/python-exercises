# Exercise: https://www.hackerrank.com/challenges/calendar-module
import calendar

array_date = [int(x) for x in input().split()]

yy = array_date[2]
mm = array_date[0]
dd = array_date[1]
day = calendar.weekday(yy, mm, dd)

# get the string representation of the current day
current_day = calendar.day_name[day]
# capitalize letters
capitalized_day = [x.upper() for x in current_day]

print("".join(capitalized_day))
