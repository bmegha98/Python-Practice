import calendar
if __name__=='__main__':
    date=list(map(int,input().split()))
    month=date[0]
    day=date[1]
    year=date[2]
    weeknum=calendar.weekday(year,month,day)
    print(calendar.day_name[weeknum].upper())
