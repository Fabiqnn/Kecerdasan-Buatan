import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

print("Fuzzy Sugeno Untuk Menentukan Tingkat Subsidi")

luasLahan = float(input("Masukkan Data Luas Lahan: "))
jumlahProduksi = float(input("Masukkan Data Produksi Padi: "))

# Rentang nilai setiap variabel
x_luasLahan = np.arange(0, 6.5, 0.5)
x_produksiPadi = np.arange(2, 8.5, 0.5)
x_tingkatSubsidi = np.arange(1, 7.5, 0.5)

# Fungsi Keanggotaan luas lahan
luasLahan_kecil = fuzz.trimf(x_luasLahan, [0, 1, 2])
luasLahan_sedang = fuzz.trimf(x_luasLahan, [1.5, 2.75, 4])
luasLahan_besar = fuzz.trimf(x_luasLahan, [3, 4.5, 6])

produksiPadi_rendah = fuzz.trimf(x_produksiPadi, [2, 3, 4])
produksiPadi_sedang = fuzz.trimf(x_produksiPadi, [3, 4.5, 6])
produksiPadi_tinggi = fuzz.trimf(x_produksiPadi, [5, 6.5, 8])

# Fungsi Keanggotaan (Output)
subsidi_rendah = 2
subsidi_sedang = 3.5
subsidi_tinggi = 5.5

# Derajat Keanggotaan Luas Lahan
mu_luasLahan_kecil = fuzz.interp_membership(x_luasLahan, luasLahan_kecil, luasLahan)
mu_luasLahan_sedang = fuzz.interp_membership(x_luasLahan, luasLahan_sedang, luasLahan)
mu_luasLahan_besar = fuzz.interp_membership(x_luasLahan, luasLahan_besar, luasLahan)

# Derajat Keanggotaan Produksi Padi
mu_produksiPadi_rendah = fuzz.interp_membership(x_produksiPadi, produksiPadi_rendah, jumlahProduksi)
mu_produksiPadi_sedang = fuzz.interp_membership(x_produksiPadi, produksiPadi_sedang, jumlahProduksi)
mu_produksiPadi_tinggi = fuzz.interp_membership(x_produksiPadi, produksiPadi_tinggi, jumlahProduksi)

# Inferensi rule
rules = [
    (min(mu_luasLahan_kecil, mu_produksiPadi_rendah), subsidi_tinggi), 
    (min(mu_luasLahan_kecil, mu_produksiPadi_sedang), subsidi_sedang), 
    (min(mu_luasLahan_kecil, mu_produksiPadi_tinggi), subsidi_rendah), 
    (min(mu_luasLahan_sedang, mu_produksiPadi_rendah), subsidi_tinggi), 
    (min(mu_luasLahan_sedang, mu_produksiPadi_sedang), subsidi_sedang), 
    (min(mu_luasLahan_sedang, mu_produksiPadi_tinggi), subsidi_rendah), 
    (min(mu_luasLahan_besar, mu_produksiPadi_rendah), subsidi_sedang), 
    (min(mu_luasLahan_besar, mu_produksiPadi_sedang), subsidi_rendah), 
    (min(mu_luasLahan_besar, mu_produksiPadi_tinggi), subsidi_rendah) 
]

perkalian_atas = sum(rule[0] * rule[1] for rule in rules)
pembagian_Bawah = sum(rule[0] for rule in rules)

if pembagian_Bawah != 0 :
    z_final = perkalian_atas / pembagian_Bawah
else:
    z_final = 0
   
print(f"Tingkat Subsidi yang Diberikan Adalah {z_final:.2f} juta")
plt.show()