def chia_hai_so_nguyen(x,y):
    if y == 0:
        return None
    else:
        return x // y
x = int(input("nhập số x: "))
y = int(input("nhập số y: "))
ket_qua = chia_hai_so_nguyen(x,y)
print(f"phần nguyên của {x} chia {y} bằng {ket_qua}")