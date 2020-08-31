import re
import datetime
'''
test array
dates= ["1900-1905","Before 1903", "18-Jun-2018","Jul-2003","26-Jul-1975.b","6-Jul-1975.b", "24-Nov-2005-", "22-Jul-144","Reported 18-Sep-2006","9-Mar-2018","   29-Oct-2011","1985","Some time between Apr & Nov-1944", "Early 1900s","2003?", "04-Feb 1993","05 May 1979"]
'''

def date_cleaner(date):
    patterns = [
        # DD-MMM-YYYY
        r'\w{1,2}-\w{3}-\w{3,4}',
        # yyyy-yyyy
        r'\d{4}-\d{4}',
        # BEFORE yyyy
        r'.*\s\d{3,4}',
        # 3) MMM-YYY
        r'\w{3}-\d{4}',
        # 4) 2014
        r'\d{4}'
    ]

    for pat in patterns:
        x = re.findall(pat, date)
        if x:
            if pat in patterns:
                date = date.split()
                return year_month_returner(date)
            else:
                return []
        else:
            return

'''
this function in called automatically from the previous one
'''
def year_month_returner(arr):
    if len(arr) == 1:
        dates = arr[0].split("-")
        for item in range(len(dates)):
            if len(dates[item]) > 4:
                dates[item] = dates[item][:4]
        return dates
    else:
        for item in arr:
            if "-" in item:
                return item.split("-")
            elif len(item) == 4 and item.isdigit():
                return [item]
            elif item[:4].isdigit() and len(item) > 4:
                return [item[:4]]


def date_month(arr):
    if arr != None:
        if len(arr) >= 3:
            return arr[1]
        elif len(arr) == 2:
            if len(arr[0]) != 3:
                return None
            else:
                return arr[0]
    else:
        return 0

def date_year(arr):
    if arr != None:
        if len(arr) >= 3:
            return arr[2]
        elif len(arr) == 2:
            return arr[1]        
        elif len(arr) == 1:
            return arr[0]
    else:
        return 0
'''
test loop
for item in dates:
    #print(date_cleaner_month(item) ,date_cleaner_year(item) )
    print(date_cleaner(item))
    #print(date_month(date_cleaner(item)))
    #print(date_year(date_cleaner(item)))
    print()
'''