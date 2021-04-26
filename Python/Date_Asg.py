import datetime
from datetime import datetime
from datetime import timedelta

# weekdays = {"sun":0 ,"mon":1,"tue":2,"wed":3,"thu":4,"fri":5,"sat":6}
# for i in weekdays:
#      print(weekdays[0])


result=0

# Employee count
print("Enter No of employees : ")
no_emp = int(input())

# Employee workings hours
print("Enter the workings hours for Employees : ")
wk_hrs = int(input())

# Starting Day
print("Enter the number between this mon-1 tue-2 wed-3 thu-4 fri-5 sat-6 sun-7  Starting Day : ")
str_day = int(input())

# Ending Day
print("Enter the number between this mon-1 tue-2 wed-3 thu-4 fri-5 sat-6 sun-7  Ending Day : ")
end_day = int(input())

tot_day= abs(end_day - str_day + 1)
#
# if str_day == 1 and end_day == 5:
#     result = wk_hrs * tot_day * no_emp
# elif str_day == 0 and end_day == 6:
#     result = wk_hrs * tot_day * no_emp
# elif str_day == 6 and end_day == 0:
#     result = wk_hrs * tot_day * no_emp
# else:
#     print("Invalid Input !! ")


week_no = [1,2,3,4,5,6,7]

for i in week_no:
    if str_day == i :
        r1 = wk_hrs * tot_day * no_emp
        break
    else:
        pass

for i in week_no:
    if end_day == i :
        r1 = wk_hrs * tot_day * no_emp
        break
    else:
        pass

print("Total Workings hours ",no_emp,"Employees is ",r1,"hrs")



# week_days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
#
# day_st=0
# day_ed=0
#
# # Starting
# for i in week_days:
#     ind= week_days.index(i)
#     if ind == str_day:
#         day_st = i
#         break
#     else:
#         pass
#
#
# # Ending
# for i in week_days:
#     indx= week_days.index(i)
#     if indx == end_day:
#         day_ed = i
#         break
#     else:
#         pass
#
#
#
# print("Total Workings hours ",no_emp,"Employees is ",result,"hrs from",day_st,"to",day_ed)




