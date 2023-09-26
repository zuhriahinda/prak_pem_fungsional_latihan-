# Sistem Penilaian Akhir Mahasiswa

# Fungsi untuk menghitung nilai akhir
def hitung_nilai_akhir(uts, uas):
    return (uts + uas) / 2

# Fungsi untuk menampilkan nilai akhir semua mahasiswa
def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print(f"{nama}: Nilai Akhir: {nilai_akhir:.2f}")

def main():
    # Data mahasiswa (nama sebagai key dan nilai UTs serta UAS sebagai value dalam bentuk dictionary)
    data_mahasiswa = {
        "Ana": hitung_nilai_akhir(85, 90),
        "Budi": hitung_nilai_akhir(78, 88),
        "Citra": hitung_nilai_akhir(92, 85),
    }

    # Menampilkan nilai akhir semua mahasiswa
    tampilkan_nilai_akhir(data_mahasiswa)

if __name__ == "__main__":
    main()
