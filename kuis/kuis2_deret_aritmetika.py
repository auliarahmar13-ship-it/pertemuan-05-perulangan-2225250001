print("Deret Aritmetika")

a = float(input("Suku pertama (a): "))
d = float(input("Beda (d): "))
n = int(input("Jumlah suku (n): "))

while d == 0 or n <= 0:
    print("Input tidak valid. Beda harus bukan 0 dan n harus positif.")
    d = float(input("Beda (d): "))
    n = int(input("Jumlah suku (n): "))

suku = a
total = 0

for i in range(1, n + 1):
    if i > 1:
        suku = suku + d

    total = total + suku

print(f"Suku: {suku}")
print(f"Jumlah: {total}")