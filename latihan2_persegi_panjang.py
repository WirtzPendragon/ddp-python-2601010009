#Program menghitung luas dan keliling persegi panjang

#Mengambil input panjang dan lebar dari user
panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))

#Menghitung luas dan keliling persegi panjang
luas = panjang * lebar
keliling = 2 * (panjang + lebar)

#Menampilkan hasil perhitungan
print(f"luas: {luas}m²\nkeliling: {keliling}m")