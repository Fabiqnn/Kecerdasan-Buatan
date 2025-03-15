import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

print("Fuzzy Sugeno Untuk Menentukan Tingkat Subsidi")
print("==============================")
luasLahan = float(input("Masukkan Data Luas Lahan: "))
jumlahProduksi = float(input("Masukkan Data Produksi Padi: "))
irigasiLahan = float(input("Masukkan Data Irigasi: "))
print("==============================")

# Rentang nilai setiap variabel
x_luasLahan = np.arange(0, 6.5, 0.5)
x_produksiPadi = np.arange(2, 8.6, 0.1)
x_irigasi = np.arange(0, 9.5, 0.5)
x_tingkatSubsidi = np.arange(1, 7.6, 0.1)

# Fungsi Keanggotaan
luasLahan_sangat_kecil = fuzz.trimf(x_luasLahan, [0, 1, 2])
luasLahan_kecil = fuzz.trimf(x_luasLahan, [1, 2, 3])
luasLahan_sedang = fuzz.trimf(x_luasLahan, [2, 3, 4])
luasLahan_besar = fuzz.trimf(x_luasLahan, [3, 4, 5])
luasLahan_sangat_besar = fuzz.trimf(x_luasLahan, [4, 5, 6])

produksiPadi_sangat_rendah = fuzz.trimf(x_produksiPadi, [2, 3, 4])
produksiPadi_rendah = fuzz.trimf(x_produksiPadi, [3, 4, 5])
produksiPadi_sedang = fuzz.trimf(x_produksiPadi, [4, 5, 6])
produksiPadi_tinggi = fuzz.trimf(x_produksiPadi, [5, 6, 7])
produksiPadi_sangat_tinggi = fuzz.trimf(x_produksiPadi, [6, 7, 8])

irigasi_sangat_buruk = fuzz.trimf(x_irigasi, [0, 1.5, 3])
irigasi_buruk = fuzz.trimf(x_irigasi, [1.5, 3, 4.5])
irigasi_sedang = fuzz.trimf(x_irigasi, [3, 4.5, 6])
irigasi_baik = fuzz.trimf(x_irigasi, [4.5, 6, 7.5])
irigasi_sangat_baik = fuzz.trimf(x_irigasi, [6, 7.5, 9])

subsidi_sangat_rendah = fuzz.trimf(x_tingkatSubsidi, [1, 2, 3])
subsidi_rendah = fuzz.trimf(x_tingkatSubsidi, [2, 3, 4])
subsidi_sedang = fuzz.trimf(x_tingkatSubsidi, [3, 4, 5])
subsidi_tinggi = fuzz.trimf(x_tingkatSubsidi, [4, 5, 6])
subsidi_sangat_tinggi = fuzz.trimf(x_tingkatSubsidi, [5, 6, 7])

# Fungsi Keanggotaan (Output)
tengahSubsidi_sangatRendah = 2
tengahSubsidi_rendah = 3
tengahSubsidi_sedang = 4
tengahSubsidi_tinggi = 5
tengahSubsidi_sangatTinggi = 6

# Derajat Keanggotaan Luas Lahan
mu_luasLahan_sangat_kecil = fuzz.interp_membership(x_luasLahan, luasLahan_sangat_kecil, luasLahan)
mu_luasLahan_kecil = fuzz.interp_membership(x_luasLahan, luasLahan_kecil, luasLahan)
mu_luasLahan_sedang = fuzz.interp_membership(x_luasLahan, luasLahan_sedang, luasLahan)
mu_luasLahan_besar = fuzz.interp_membership(x_luasLahan, luasLahan_besar, luasLahan)
mu_luasLahan_sangat_besar = fuzz.interp_membership(x_luasLahan, luasLahan_sangat_besar, luasLahan)

# Derajat Keanggotaan Produksi Padi
mu_produksiPadi_sangat_rendah = fuzz.interp_membership(x_produksiPadi, produksiPadi_sangat_rendah, jumlahProduksi)
mu_produksiPadi_rendah = fuzz.interp_membership(x_produksiPadi, produksiPadi_rendah, jumlahProduksi)
mu_produksiPadi_sedang = fuzz.interp_membership(x_produksiPadi, produksiPadi_sedang, jumlahProduksi)
mu_produksiPadi_tinggi = fuzz.interp_membership(x_produksiPadi, produksiPadi_tinggi, jumlahProduksi)
mu_produksiPadi_sangat_tinggi = fuzz.interp_membership(x_produksiPadi, produksiPadi_sangat_tinggi, jumlahProduksi)


# Derajat Keanggotaan Irigasi
mu_irigasi_sangat_buruk= fuzz.interp_membership(x_irigasi, irigasi_sangat_buruk, irigasiLahan)
mu_irigasi_buruk= fuzz.interp_membership(x_irigasi, irigasi_buruk, irigasiLahan)
mu_irigasi_sedang= fuzz.interp_membership(x_irigasi, irigasi_sedang, irigasiLahan)
mu_irigasi_baik= fuzz.interp_membership(x_irigasi, irigasi_baik, irigasiLahan)
mu_irigasi_sangat_baik= fuzz.interp_membership(x_irigasi, irigasi_sangat_baik, irigasiLahan)

# Inferensi rule
rules = [
    (min(mu_luasLahan_sangat_kecil, mu_produksiPadi_sangat_rendah, mu_irigasi_sangat_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sangat_kecil, mu_produksiPadi_rendah, mu_irigasi_sangat_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sangat_kecil, mu_produksiPadi_sedang, mu_irigasi_sangat_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sangat_kecil, mu_produksiPadi_tinggi, mu_irigasi_sangat_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sangat_kecil, mu_produksiPadi_sangat_tinggi, mu_irigasi_sangat_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_kecil, mu_produksiPadi_sangat_rendah, mu_irigasi_sangat_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_kecil, mu_produksiPadi_rendah, mu_irigasi_sangat_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_kecil, mu_produksiPadi_sedang, mu_irigasi_sangat_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_kecil, mu_produksiPadi_tinggi, mu_irigasi_sangat_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_kecil, mu_produksiPadi_sangat_tinggi, mu_irigasi_sangat_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sedang, mu_produksiPadi_sangat_rendah, mu_irigasi_sangat_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sedang, mu_produksiPadi_rendah, mu_irigasi_sangat_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sedang, mu_produksiPadi_sedang, mu_irigasi_sangat_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sedang, mu_produksiPadi_tinggi, mu_irigasi_sangat_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sedang, mu_produksiPadi_sangat_tinggi, mu_irigasi_sangat_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_besar, mu_produksiPadi_sangat_rendah, mu_irigasi_sangat_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_besar, mu_produksiPadi_rendah, mu_irigasi_sangat_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_besar, mu_produksiPadi_sedang, mu_irigasi_sangat_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_besar, mu_produksiPadi_tinggi, mu_irigasi_sangat_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_besar, mu_produksiPadi_sangat_tinggi, mu_irigasi_sangat_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sangat_besar, mu_produksiPadi_sangat_rendah, mu_irigasi_sangat_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sangat_besar, mu_produksiPadi_rendah, mu_irigasi_sangat_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sangat_besar, mu_produksiPadi_sedang, mu_irigasi_sangat_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sangat_besar, mu_produksiPadi_tinggi, mu_irigasi_sangat_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sangat_besar, mu_produksiPadi_sangat_tinggi, mu_irigasi_sangat_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sangat_kecil, mu_produksiPadi_sangat_rendah, mu_irigasi_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sangat_kecil, mu_produksiPadi_rendah, mu_irigasi_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sangat_kecil, mu_produksiPadi_sedang, mu_irigasi_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sangat_kecil, mu_produksiPadi_tinggi, mu_irigasi_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sangat_kecil, mu_produksiPadi_sangat_tinggi, mu_irigasi_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_kecil, mu_produksiPadi_sangat_rendah, mu_irigasi_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_kecil, mu_produksiPadi_rendah, mu_irigasi_buruk), tengahSubsidi_tinggi),
    (min(mu_luasLahan_kecil, mu_produksiPadi_sedang, mu_irigasi_buruk), tengahSubsidi_tinggi),
    (min(mu_luasLahan_kecil, mu_produksiPadi_tinggi, mu_irigasi_buruk), tengahSubsidi_tinggi),
    (min(mu_luasLahan_kecil, mu_produksiPadi_sangat_tinggi, mu_irigasi_buruk), tengahSubsidi_tinggi),
    (min(mu_luasLahan_sedang, mu_produksiPadi_sangat_rendah, mu_irigasi_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sedang, mu_produksiPadi_rendah, mu_irigasi_buruk), tengahSubsidi_tinggi),
    (min(mu_luasLahan_sedang, mu_produksiPadi_sedang, mu_irigasi_buruk), tengahSubsidi_tinggi),
    (min(mu_luasLahan_sedang, mu_produksiPadi_tinggi, mu_irigasi_buruk), tengahSubsidi_tinggi),
    (min(mu_luasLahan_sedang, mu_produksiPadi_sangat_tinggi, mu_irigasi_buruk), tengahSubsidi_tinggi),
    (min(mu_luasLahan_besar, mu_produksiPadi_sangat_rendah, mu_irigasi_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_besar, mu_produksiPadi_rendah, mu_irigasi_buruk), tengahSubsidi_tinggi),
    (min(mu_luasLahan_besar, mu_produksiPadi_sedang, mu_irigasi_buruk), tengahSubsidi_tinggi),
    (min(mu_luasLahan_besar, mu_produksiPadi_tinggi, mu_irigasi_buruk), tengahSubsidi_tinggi),
    (min(mu_luasLahan_besar, mu_produksiPadi_sangat_tinggi, mu_irigasi_buruk), tengahSubsidi_tinggi),
    (min(mu_luasLahan_sangat_besar, mu_produksiPadi_sangat_rendah, mu_irigasi_buruk), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sangat_besar, mu_produksiPadi_rendah, mu_irigasi_buruk), tengahSubsidi_tinggi),
    (min(mu_luasLahan_sangat_besar, mu_produksiPadi_sedang, mu_irigasi_buruk), tengahSubsidi_tinggi),
    (min(mu_luasLahan_sangat_besar, mu_produksiPadi_tinggi, mu_irigasi_buruk), tengahSubsidi_tinggi),
    (min(mu_luasLahan_sangat_besar, mu_produksiPadi_sangat_tinggi, mu_irigasi_buruk), tengahSubsidi_tinggi),
    (min(mu_luasLahan_sangat_kecil, mu_produksiPadi_sangat_rendah, mu_irigasi_sedang), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sangat_kecil, mu_produksiPadi_rendah, mu_irigasi_sedang), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sangat_kecil, mu_produksiPadi_sedang, mu_irigasi_sedang), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sangat_kecil, mu_produksiPadi_tinggi, mu_irigasi_sedang), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sangat_kecil, mu_produksiPadi_sangat_tinggi, mu_irigasi_sedang), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_kecil, mu_produksiPadi_sangat_rendah, mu_irigasi_sedang), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_kecil, mu_produksiPadi_rendah, mu_irigasi_sedang), tengahSubsidi_tinggi),
    (min(mu_luasLahan_kecil, mu_produksiPadi_sedang, mu_irigasi_sedang), tengahSubsidi_tinggi),
    (min(mu_luasLahan_kecil, mu_produksiPadi_tinggi, mu_irigasi_sedang), tengahSubsidi_tinggi),
    (min(mu_luasLahan_kecil, mu_produksiPadi_sangat_tinggi, mu_irigasi_sedang), tengahSubsidi_tinggi),
    (min(mu_luasLahan_sedang, mu_produksiPadi_sangat_rendah, mu_irigasi_sedang), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sedang, mu_produksiPadi_rendah, mu_irigasi_sedang), tengahSubsidi_tinggi),
    (min(mu_luasLahan_sedang, mu_produksiPadi_sedang, mu_irigasi_sedang), tengahSubsidi_sedang),
    (min(mu_luasLahan_sedang, mu_produksiPadi_tinggi, mu_irigasi_sedang), tengahSubsidi_sedang),
    (min(mu_luasLahan_sedang, mu_produksiPadi_sangat_tinggi, mu_irigasi_sedang), tengahSubsidi_sedang),
    (min(mu_luasLahan_besar, mu_produksiPadi_sangat_rendah, mu_irigasi_sedang), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_besar, mu_produksiPadi_rendah, mu_irigasi_sedang), tengahSubsidi_tinggi),
    (min(mu_luasLahan_besar, mu_produksiPadi_sedang, mu_irigasi_sedang), tengahSubsidi_sedang),
    (min(mu_luasLahan_besar, mu_produksiPadi_tinggi, mu_irigasi_sedang), tengahSubsidi_sedang),
    (min(mu_luasLahan_besar, mu_produksiPadi_sangat_tinggi, mu_irigasi_sedang), tengahSubsidi_sedang),
    (min(mu_luasLahan_sangat_besar, mu_produksiPadi_sangat_rendah, mu_irigasi_sedang), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sangat_besar, mu_produksiPadi_rendah, mu_irigasi_sedang), tengahSubsidi_tinggi),
    (min(mu_luasLahan_sangat_besar, mu_produksiPadi_sedang, mu_irigasi_sedang), tengahSubsidi_sedang),
    (min(mu_luasLahan_sangat_besar, mu_produksiPadi_tinggi, mu_irigasi_sedang), tengahSubsidi_sedang),
    (min(mu_luasLahan_sangat_besar, mu_produksiPadi_sangat_tinggi, mu_irigasi_sedang), tengahSubsidi_sedang),
    (min(mu_luasLahan_sangat_kecil, mu_produksiPadi_sangat_rendah, mu_irigasi_baik), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sangat_kecil, mu_produksiPadi_rendah, mu_irigasi_baik), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sangat_kecil, mu_produksiPadi_sedang, mu_irigasi_baik), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sangat_kecil, mu_produksiPadi_tinggi, mu_irigasi_baik), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sangat_kecil, mu_produksiPadi_sangat_tinggi, mu_irigasi_baik), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_kecil, mu_produksiPadi_sangat_rendah, mu_irigasi_baik), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_kecil, mu_produksiPadi_rendah, mu_irigasi_baik), tengahSubsidi_tinggi),
    (min(mu_luasLahan_kecil, mu_produksiPadi_sedang, mu_irigasi_baik), tengahSubsidi_tinggi),
    (min(mu_luasLahan_kecil, mu_produksiPadi_tinggi, mu_irigasi_baik), tengahSubsidi_tinggi),
    (min(mu_luasLahan_kecil, mu_produksiPadi_sangat_tinggi, mu_irigasi_baik), tengahSubsidi_tinggi),
    (min(mu_luasLahan_sedang, mu_produksiPadi_sangat_rendah, mu_irigasi_baik), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sedang, mu_produksiPadi_rendah, mu_irigasi_baik), tengahSubsidi_tinggi),
    (min(mu_luasLahan_sedang, mu_produksiPadi_sedang, mu_irigasi_baik), tengahSubsidi_sedang),
    (min(mu_luasLahan_sedang, mu_produksiPadi_tinggi, mu_irigasi_baik), tengahSubsidi_sedang),
    (min(mu_luasLahan_sedang, mu_produksiPadi_sangat_tinggi, mu_irigasi_baik), tengahSubsidi_sedang),
    (min(mu_luasLahan_besar, mu_produksiPadi_sangat_rendah, mu_irigasi_baik), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_besar, mu_produksiPadi_rendah, mu_irigasi_baik), tengahSubsidi_tinggi),
    (min(mu_luasLahan_besar, mu_produksiPadi_sedang, mu_irigasi_baik), tengahSubsidi_sedang),
    (min(mu_luasLahan_besar, mu_produksiPadi_tinggi, mu_irigasi_baik), tengahSubsidi_rendah),
    (min(mu_luasLahan_besar, mu_produksiPadi_sangat_tinggi, mu_irigasi_baik), tengahSubsidi_rendah),
    (min(mu_luasLahan_sangat_besar, mu_produksiPadi_sangat_rendah, mu_irigasi_baik), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sangat_besar, mu_produksiPadi_rendah, mu_irigasi_baik), tengahSubsidi_tinggi),
    (min(mu_luasLahan_sangat_besar, mu_produksiPadi_sedang, mu_irigasi_baik), tengahSubsidi_sedang),
    (min(mu_luasLahan_sangat_besar, mu_produksiPadi_tinggi, mu_irigasi_baik), tengahSubsidi_rendah),
    (min(mu_luasLahan_sangat_besar, mu_produksiPadi_sangat_tinggi, mu_irigasi_baik), tengahSubsidi_rendah),
    (min(mu_luasLahan_sangat_kecil, mu_produksiPadi_sangat_rendah, mu_irigasi_sangat_baik), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sangat_kecil, mu_produksiPadi_rendah, mu_irigasi_sangat_baik), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sangat_kecil, mu_produksiPadi_sedang, mu_irigasi_sangat_baik), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sangat_kecil, mu_produksiPadi_tinggi, mu_irigasi_sangat_baik), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sangat_kecil, mu_produksiPadi_sangat_tinggi, mu_irigasi_sangat_baik), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_kecil, mu_produksiPadi_sangat_rendah, mu_irigasi_sangat_baik), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_kecil, mu_produksiPadi_rendah, mu_irigasi_sangat_baik), tengahSubsidi_tinggi),
    (min(mu_luasLahan_kecil, mu_produksiPadi_sedang, mu_irigasi_sangat_baik), tengahSubsidi_tinggi),
    (min(mu_luasLahan_kecil, mu_produksiPadi_tinggi, mu_irigasi_sangat_baik), tengahSubsidi_tinggi),
    (min(mu_luasLahan_kecil, mu_produksiPadi_sangat_tinggi, mu_irigasi_sangat_baik), tengahSubsidi_tinggi),
    (min(mu_luasLahan_sedang, mu_produksiPadi_sangat_rendah, mu_irigasi_sangat_baik), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sedang, mu_produksiPadi_rendah, mu_irigasi_sangat_baik), tengahSubsidi_tinggi),
    (min(mu_luasLahan_sedang, mu_produksiPadi_sedang, mu_irigasi_sangat_baik), tengahSubsidi_sedang),
    (min(mu_luasLahan_sedang, mu_produksiPadi_tinggi, mu_irigasi_sangat_baik), tengahSubsidi_sedang),
    (min(mu_luasLahan_sedang, mu_produksiPadi_sangat_tinggi, mu_irigasi_sangat_baik), tengahSubsidi_sedang),
    (min(mu_luasLahan_besar, mu_produksiPadi_sangat_rendah, mu_irigasi_sangat_baik), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_besar, mu_produksiPadi_rendah, mu_irigasi_sangat_baik), tengahSubsidi_tinggi),
    (min(mu_luasLahan_besar, mu_produksiPadi_sedang, mu_irigasi_sangat_baik), tengahSubsidi_sedang),
    (min(mu_luasLahan_besar, mu_produksiPadi_tinggi, mu_irigasi_sangat_baik), tengahSubsidi_rendah),
    (min(mu_luasLahan_besar, mu_produksiPadi_sangat_tinggi, mu_irigasi_sangat_baik), tengahSubsidi_rendah),
    (min(mu_luasLahan_sangat_besar, mu_produksiPadi_sangat_rendah, mu_irigasi_sangat_baik), tengahSubsidi_sangatTinggi),
    (min(mu_luasLahan_sangat_besar, mu_produksiPadi_rendah, mu_irigasi_sangat_baik), tengahSubsidi_tinggi),
    (min(mu_luasLahan_sangat_besar, mu_produksiPadi_sedang, mu_irigasi_sangat_baik), tengahSubsidi_sedang),
    (min(mu_luasLahan_sangat_besar, mu_produksiPadi_tinggi, mu_irigasi_sangat_baik), tengahSubsidi_rendah),
    (min(mu_luasLahan_sangat_besar, mu_produksiPadi_sangat_tinggi, mu_irigasi_sangat_baik), tengahSubsidi_sangatRendah)
]


perkalian_atas = sum(rule[0] * rule[1] for rule in rules)
pembagian_Bawah = sum(rule[0] for rule in rules)

if pembagian_Bawah != 0 :
    z_final = perkalian_atas / pembagian_Bawah
else:
    z_final = 0
print(f"Tingkat Subsidi yang Diberikan Adalah {z_final:.2f} juta")


# Grafik Fungsi Keanggotaan Luas Lahan
plt.figure(figsize=(12, 9))

plt.subplot(4, 1, 1)
plt.plot(x_luasLahan, luasLahan_sangat_kecil, label="Sangat Kecil", color='brown')
plt.plot(x_luasLahan, luasLahan_kecil, label="Kecil", color='blue')
plt.plot(x_luasLahan, luasLahan_sedang, label="Sedang", color='green')
plt.plot(x_luasLahan, luasLahan_besar, label="Besar", color='orange')
plt.plot(x_luasLahan, luasLahan_sangat_besar, label="Besar", color='red')
plt.axvline(x=luasLahan, color='black', linestyle='--', label="Input Data")
plt.title("Fungsi Keanggotaan Luas Lahan")
plt.xlabel("Luas Lahan (ha)")
plt.ylabel("Derajat Keanggotaan")
plt.legend()

# Grafik Fungsi Keanggotaan Produksi Padi
plt.subplot(4, 1, 2)
plt.plot(x_produksiPadi, produksiPadi_sangat_rendah, label="Sangat Rendah", color='brown')
plt.plot(x_produksiPadi, produksiPadi_rendah, label="Rendah", color='blue')
plt.plot(x_produksiPadi, produksiPadi_sedang, label="Sedang", color='green')
plt.plot(x_produksiPadi, produksiPadi_tinggi, label="Tinggi", color='orange')
plt.plot(x_produksiPadi, produksiPadi_sangat_tinggi, label="Sangat Tinggi", color='red')
plt.axvline(x=jumlahProduksi, color='black', linestyle='--', label="Input Data")
plt.title("Fungsi Keanggotaan Produksi Padi")
plt.xlabel("Produksi Padi (ton/ha)")
plt.ylabel("Derajat Keanggotaan")
plt.legend()

# Grafik Fungsi Keanggotaan Irigasi
plt.subplot(4, 1, 3)
plt.plot(x_irigasi, irigasi_sangat_buruk, label="Sangat Buruk")
plt.plot(x_irigasi, irigasi_buruk, label="Buruk")
plt.plot(x_irigasi, irigasi_sedang, label="Sedang")
plt.plot(x_irigasi, irigasi_baik, label="Baik")
plt.plot(x_irigasi, irigasi_sangat_baik, label="Sangat Baik")
plt.axvline(x=irigasiLahan, color="black", linestyle='--', label="Input Data")
plt.title("Fungsi Keanggotaan Irigasi")
plt.xlabel("Irigasi (L/s)")
plt.ylabel("Derajat Keanggotaan")
plt.legend()


# Grafik Output Subsidi (Hasil Sugeno)
plt.subplot(4, 1, 4)
plt.plot(x_tingkatSubsidi, subsidi_sangat_rendah, label="Rendah", color='brown')
plt.plot(x_tingkatSubsidi, subsidi_rendah, label="Rendah", color='blue')
plt.plot(x_tingkatSubsidi, subsidi_sedang, label="Sedang", color='green')
plt.plot(x_tingkatSubsidi, subsidi_tinggi, label="Tinggi", color='orange')
plt.plot(x_tingkatSubsidi, subsidi_sangat_tinggi, label="Tinggi", color='red')
plt.axvline(x=z_final, color='black', linestyle='--', label=f"Hasil: {z_final:.2f}")
plt.title("Output Tingkat Subsidi")
plt.xlabel("Tingkat Subsidi (juta rupiah)")
plt.ylabel("Output Sugeno")
plt.legend()

plt.tight_layout()  
plt.show()