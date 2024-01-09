def so_hoan_hao(x):
    tong_uoc = 0
    for i in range(1,x):
        if x % i == 0:
            tong_uoc += i 
    return tong_uoc == x
x = eval(input("nhập số cần kiểm tra: "))
ket_qua = so_hoan_hao(x)
if ket_qua:
    print(f"{x} là số hoàn hảo")
else:
    print(f"{x} không phải là số hoàn hảo")


