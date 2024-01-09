def A(n,x):
    A = (x*x + x + 1)**n + (x*x - x + 1)**n
    return A
n = eval(input("nhập số n: "))
x = eval(input("nhập số x: "))
A = A(n,x)
print(f"kết quả A= {A}")