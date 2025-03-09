import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl
import matplotlib.pyplot as plt

luas_lahan = ctrl.Antecedent(np.arange(0, 6.1, 0.1), 'luas_lahan')
produksi_padi = ctrl.Antecedent(np.arange(2, 8.1, 0.1), 'produksi_padi')
subsidi = ctrl.Consequent(np.arange(1, 7.1, 0.1), 'subsidi')

luas_lahan['kecil'] = fuzz.trimf(luas_lahan.universe, [0, 1, 2])
luas_lahan['sedang'] = fuzz.trimf(luas_lahan.universe, [1.5, 2.75, 4])
luas_lahan['besar'] = fuzz.trimf(luas_lahan.universe, [3, 4.5, 6])

produksi_padi['rendah'] = fuzz.trimf(produksi_padi.universe, [2, 3, 4])
produksi_padi['sedang'] = fuzz.trimf(produksi_padi.universe, [3, 4.5, 6])
produksi_padi['tinggi'] = fuzz.trimf(produksi_padi.universe, [5, 6.5, 8])

subsidi['rendah'] = fuzz.trimf(subsidi.universe, [1, 2, 3])
subsidi['sedang'] = fuzz.trimf(subsidi.universe, [2, 3.5, 5])
subsidi['tinggi'] = fuzz.trimf(subsidi.universe, [4, 5.5, 7])

rule1 = ctrl.Rule(luas_lahan['kecil'] & produksi_padi['rendah'], subsidi['tinggi'])
rule2 = ctrl.Rule(luas_lahan['kecil'] & produksi_padi['sedang'], subsidi['sedang'])
rule3 = ctrl.Rule(luas_lahan['kecil'] & produksi_padi['tinggi'], subsidi['rendah'])
rule4 = ctrl.Rule(luas_lahan['sedang'] & produksi_padi['rendah'], subsidi['tinggi'])
rule5 = ctrl.Rule(luas_lahan['sedang'] & produksi_padi['sedang'], subsidi['sedang'])
rule6 = ctrl.Rule(luas_lahan['sedang'] & produksi_padi['tinggi'], subsidi['rendah'])
rule7 = ctrl.Rule(luas_lahan['besar'] & produksi_padi['rendah'], subsidi['sedang'])
rule8 = ctrl.Rule(luas_lahan['besar'] & produksi_padi['sedang'], subsidi['rendah'])
rule9 = ctrl.Rule(luas_lahan['besar'] & produksi_padi['tinggi'], subsidi['rendah'])

subsidi_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
subsidi_simulasi = ctrl.ControlSystemSimulation(subsidi_ctrl)

# Input data petani
subsidi_simulasi.input['luas_lahan'] = 3.2
subsidi_simulasi.input['produksi_padi'] = 5.0

# Proses inferensi dan defuzzifikasi
subsidi_simulasi.compute()

# Output hasil
print(f"Tingkat subsidi yang diberikan: {subsidi_simulasi.output['subsidi']:.2f} juta rupiah per hektar")
subsidi.view(sim=subsidi_simulasi)
