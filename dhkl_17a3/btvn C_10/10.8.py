import datetime
day = int(input("nhập ngày: "))
month = int(input("nhập tháng: "))
year = int(input("nhập năm: "))
print(f"ngày tháng năm của bạn là: {day}/{month}/{year}.")
#kiểm tra năm nhuận:
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"năm {year} là năm nhuận.")
else:
    print(f"năm {year} không phải là năm nhuận.")
#kiểm tra xem ngày tháng năm đó là thứ mấy:
date = datetime.date(year, month, day)
thu_trong_tuan = date.strftime("%A")
print(f"{day}/{month}/{year} là thứ {thu_trong_tuan}")
#kiểm tra xem tháng nhập vào có bao nhiêu ngày:
import calendar
so_ngay = calendar.monthrange(year, month)[1]
print(f"tháng {month} có: {so_ngay} ngày.")    


