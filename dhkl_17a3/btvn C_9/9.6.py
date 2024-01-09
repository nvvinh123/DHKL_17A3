def kiem_tra_so_nguyen_to(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
        else:
            return True
x = int(input("nhập số cần kiểm tra: "))
x = kiem_tra_so_nguyen_to(x)
print(f" {x} ")