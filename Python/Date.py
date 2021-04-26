import datetime
from datetime import datetime
from datetime import timedelta

# cur_date = datetime.now()
# print(cur_date.strftime("%d / %m / %Y"))
# print(cur_date.strftime("%H : %M : %S "))

# t1 = datetime.time(8, 30, 00)
# t2 = datetime.time(16, 30, 00)

# st= "2021-03-01 00:00:00"
# ed= "2021-03-06 00:00:00"
# datetimeFormat = '%Y-%m-%d %H:%M:%S'
# t = datetime.strptime(st,datetimeFormat)
# print(t)

t1 = datetime(2021,3,1,00,00,00)
t2 = datetime(2021,3,6,00,00,00)

d1 = t1.day
d2 = t2.day
# print(d2)

# print("Start Date :",t1.strftime("%d / %m / %Y"))
# print("End Date : ",t2.strftime("%d / %m / %Y"))
# print("Totals days:",t2.day - t1.day)

# timedelta = t2 - t1
# print(timedelta)

# total_seconds = timedelta.total_seconds()
# minutes = total_seconds/60
# print(minutes)
# minutes = divmod(total_seconds, 60)
# print('Total difference in minutes: ', minutes[0], 'minutes',minutes[1], 'seconds')

# print(timedelta.days * 24 * 3600 + timedelta.seconds)

# new = timedelta(days=1)
# datetime.timedelta(days=1).strftime('%Y-%m-%d %H:%M:%S')
# print(new + t1)

# for d1 > d2 :
#     print()

tot_hrs=0

while(t1.date() <= t2.date()):
    tot_hrs += tot_hrs ++ 8
    new = timedelta(days=1)
    # new + t1.date()
    # print(new + t1.date())
    break


result = 15 * tot_hrs
print("Total hours worked by 15 employees form ",t1,"to",t2, "is : ",result,"hrs")

    # tdelta = timedelta(days = 1)
    # print(tdelta + t1)

# x = t1.strftime("%H : %M : %S :%M ")

week_no = [0,1,2,3,4,5,6]

start_day = 5
end_day = 0
no_emp=15
work_hrs = 8
total_days = abs(end_day - start_day) - 7
total = abs(total_days)
print(total)

for i in week_no:
    if start_day == i :
        for j in reversed(week_no):
            if end_day == j:
                r1 = no_emp * work_hrs * total
            else:
                pass
    else:
        pass


print(r1,"hrs")