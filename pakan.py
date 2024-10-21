# Fungsi untuk menghitung biaya dan memeriksa batasan
def hitung_biaya(kg_A, kg_B):
    protein = 3 * kg_A + 2 * kg_B
    energi = 2 * kg_A + 4 * kg_B
    biaya = 10000 * kg_A + 8000 * kg_B
    
    return protein, energi, biaya

# Input jumlah bahan pakan A dan B
kg_A = float(input("Masukkan jumlah bahan pakan A (kg): "))
kg_B = float(input("Masukkan jumlah bahan pakan B (kg): "))

# Hitung protein, energi, dan biaya
protein, energi, biaya = hitung_biaya(kg_A, kg_B)

# Periksa apakah batasan terpenuhi
if protein >= 18 and energi >= 24:
    print(f"Bahan pakan A yang digunakan: {kg_A:.2f} kg")
    print(f"Bahan pakan B yang digunakan: {kg_B:.2f} kg")
    print(f"Total biaya: {biaya:.2f} rupiah")
else:
    print("Kombinasi ini tidak memenuhi batasan minimum untuk protein dan energi.")
