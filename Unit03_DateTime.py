# --- no.01 日付の取得
import datetime

today = datetime.date.today()
todaydetail = datetime.datetime.today()

# 今日の日付
print('--------------------------------')
print(today)
print(todaydetail)
print('--------------------------------')
print(today.year)
print(today.month)
print(today.day)
print('--------------------------------')
print(todaydetail.year)
print(todaydetail.month)
print(todaydetail.day)
print(todaydetail.hour)
print(todaydetail.minute)
print(todaydetail.second)
print(todaydetail.microsecond)
print('--------------------------------')

# 日付のフォーマット
print(today.isoformat())
print(todaydetail.strftime("%Y/%m/%d %H:%M:%S"))

# --- no.02 日付の計算
today = datetime.datetime.today()

print(today)																	# 今日の日付
print(today + datetime.timedelta(days = 1))		# 明日の日付

newyear = datetime.datetime(2018, 1, 1)
print(newyear + datetime.timedelta(days = 7))	# 2018.01.01の1週間後

calc = today - newyear
print(calc.days)

# --- no.03 閏年の判定
import calendar
print(calendar.isleap(2015))
print(calendar.isleap(2016))
print(calendar.isleap(2017))
print(calendar.leapdays(2010, 2020))

