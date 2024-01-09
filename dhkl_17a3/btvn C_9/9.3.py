def tinh_bmi(can_nang,chieu_cao):
    bmi = can_nang / (chieu_cao **2)
    return bmi
can_nang = float(input("cân nặng của bạn là: "))
chieu_cao = float(input("chiều cao của bạn là: "))
bmi = tinh_bmi(can_nang,chieu_cao)
print(f"chỉ số BMI của bạn là: {bmi}")
