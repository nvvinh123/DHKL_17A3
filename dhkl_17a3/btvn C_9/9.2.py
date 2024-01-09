nam = int(input("năm bạn muốn kiểm tra: "))
#tính can:
def tinh_can(nam):
    can = nam % 10
    if can == 0:
        return("canh")
    elif can == 1:
        return("tân")
    elif can == 2:
        return("nhâm")
    elif can == 3:
        return("quý")
    elif can == 4:
        return("giáp")
    elif can == 5:
        return("ất")
    elif can == 6:
        return("bính")
    elif can == 7:
        return("đinh")
    elif can == 8:
        return("mậu")
    else:
        return("kỳ")     
#tính chi:
def tinh_chi(nam):
    chi = nam % 12
    if chi == 0:
        return("thân")
    elif chi == 1:
        return("dậu")
    elif chi == 2:
        return("tuất")
    elif chi == 3:
        return("hợi")
    elif chi == 4:
        return("tý")
    elif chi == 5:
        return("sửu")
    elif chi == 6:
        return("dần")
    elif chi == 7:
        return("mão")
    elif chi == 8:
        return("thìn")
    elif chi == 9:
        return("tỵ")
    elif chi == 10:
        return("ngọ")
    else:
        return("mùi") 
print(f"năm {nam} lịch âm là năm {tinh_can(nam)} {tinh_chi(nam)}")

