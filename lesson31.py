from datetime import date, datetime
import locale
locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')

today = date.today()
now = datetime.now()

print(today.strftime('%x'))
print(now.strftime('%X'))