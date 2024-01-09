def kiem_tra_ma_zip(zip_code):
    if len(zip_code) == 6 and zip_code.isdigit():
        return True
    else:
        return False
zip_code = input("nhập mã zip cần kiểm tra: ")
if kiem_tra_ma_zip(zip_code):
    print(f"vậy zip code {zip_code} hợp lệ")
else:
    print(f"vậy zip code {zip_code} không hợp lệ")

 