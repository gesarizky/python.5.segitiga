import math # math module
 
# Proses Penginputan
alas = float(input('Tulis Alas Segitiga: '))
tinggi = float(input('Tulis tinggi Segitiga: '))

# Hitung Luas dan Keliling persegi
luas = alas * tinggi / 2
alasmiring = alas / 2
miring = math.sqrt(tinggi ** 2 + alasmiring ** 2)
keliling = alas + miring + miring

#Menampilkan Hasil Perhitungan
print('Luas Segitiga adalah %0.2f' %luas)
print('keliling Segitiga adalah %0.2f' %keliling)
