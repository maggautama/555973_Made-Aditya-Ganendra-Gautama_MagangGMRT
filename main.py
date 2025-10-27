import numpy as np

lengan1 = float(input("Panjang lengan 1 : "))
lengan2 = float(input("Panjang lengan 2 : "))
lengan3 = float(input("Panjang lengan 3 : "))
s1 = float(input("Masukkan sudut rotasi θ1 (derajat): "))
s2 = float(input("Masukkan sudut rotasi θ2 (derajat): "))
s3 = float(input("Masukkan sudut rotasi θ3 (derajat): "))

rads1 = np.radians(s1)
rads2 = np.radians(s2)
rads3 = np.radians(s3)

x1 = np.cos(rads1)*lengan1
y1 = np.sin(rads1)*lengan1
x2 = x1+(np.cos(rads1+rads2)*lengan2)
y2 = y1+(np.sin(rads1+rads2)*lengan2)
x3 = x2+(np.cos(rads1+rads2+rads3)*lengan3)
y3 = y2+(np.sin(rads1+rads2+rads3)*lengan3)

print("\nHasil : ")
print(f"Koordinat setelah DOF 1 (x1, y1): ({x1:.2f}, {y1:.2f})")
print(f"Koordinat setelah DOF 2 (x2, y2): ({x2:.2f}, {y2:.2f})")
print(f"Koordinat akhir (x3, y3): ({x3:.2f}, {y3:.2f})")
