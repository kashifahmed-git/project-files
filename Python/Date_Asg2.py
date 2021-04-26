import datetime
from datetime import date
from datetime import timedelta
import calendar

"""
t1 = datetime.datetime.strptime("2021-3-1","%Y-%m-%d")
start_day = date.isoweekday(t1)
print(start_day)

t2 = datetime.datetime.strptime("2021,3,8","%Y,%m,%d")
# end_day = date.isoweekday(t2)
end = calendar.weekday(2021,3,8)
print(end)


week_days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
weekday = calendar.weekday(2021,3,1)
print(week_days[weekday])


Find the total workings hours of employees from start day and end day ?
Get input for employee working hrs,number of employee and get start day and end day using weekday number(like mon-0...sun-6)only.  
Find total working days and then Calculate the total workings hours of an employee from start day and end day .


"""

# Employee count
print("Enter Nubmer of employees : ")
no_emp = int(input())

# Employee workings hours
print("Enter the workings hours for Employees : ")
work_hrs =float(input())

# Starting Day
print("Enter the number between this Mon-0 Tue-1 Wed-2 Thu-3 Fri-4 Sat-5 Sun-6  Starting Day : ")
start_day = int(input())

# Ending Day
print("Enter the number between this Mon-0 Tue-1 Wed-2 Thu-3 Fri-4 Sat-5 Sun-6  Ending Day : ")
end_day = int(input())

total=0
total_days = 0

if start_day == end_day:
    total = abs(start_day - end_day) + 7
    total_days = abs(total) + 1
elif start_day > end_day:
    total = abs(start_day - end_day) - 7
    total_days = abs(total) + 1
elif start_day < end_day:
    total = abs(end_day - start_day)
    total_days = abs(total) + 1

week_no = [0,1,2,3,4,5,6]

for i in week_no:
    if start_day == i :
        for j in week_no:
            if end_day == j:
                result = no_emp * work_hrs * total_days
            else:
                pass
    else:
        pass

# print("Total Workings hours ",no_emp,"Employees is ",result,"hrs")

week_days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

day_st=0
day_ed=0

# Starting
for i in week_days:
    ind= week_days.index(i)
    if ind == start_day:
        day_st = i
        break
    else:
        pass

# Ending
for i in week_days:
    indx= week_days.index(i)
    if indx == end_day:
        day_ed = i
        break
    else:
        pass

print("Total Workings hours ",no_emp,"Employees is ",result,"hrs from",day_st,"to",day_ed)
