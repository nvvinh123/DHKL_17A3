import math
S_tron = lambda r : math.pi * (r**2)
P_tron = lambda r : 2*math.pi * r

S_hcn = lambda a,b : a*b
P_hcn = lambda a,b : (a+b)*2

r = float(input("nhập giá trị r: "))
a = float(input("nhập giá trị a: "))
b = float(input("nhập giá trị b: "))

dien_tich_hinh_tron = S_tron(r)
chu_vi_hinh_tron = P_tron(r)
dien_tich_hinh_chu_nhat = S_hcn(a,b)
chu_vi_hinh_chu_nhat = P_hcn(a,b)

print(f"diện tích hình tròn là: {dien_tich_hinh_tron}")
print(f"diện tích hình chữ nhật là: {dien_tich_hinh_chu_nhat}")
print(f"chu vi hình tròn là: {chu_vi_hinh_tron}")
print(f"chu vi hình chữ nhật là: {chu_vi_hinh_chu_nhat}")