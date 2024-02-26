def hitung_gaji(gaji_pokok, uang_transport_harian, uang_makan_harian, tunjangan_jabatan, honor_lembur_per_jam, jumlah_jam_lembur, jumlah_hari_kerja):
    total_gaji = gaji_pokok + (uang_transport_harian * jumlah_hari_kerja) + (uang_makan_harian * jumlah_hari_kerja) + tunjangan_jabatan + (honor_lembur_per_jam * jumlah_jam_lembur)
    return total_gaji

# Meminta input dari pengguna
gaji_pokok = float(input("Masukkan gaji pokok: "))
uang_transport_harian = float(input("Masukkan uang transport harian: "))
uang_makan_harian = float(input("Masukkan uang makan harian: "))
tunjangan_jabatan = float(input("Masukkan tunjangan jabatan: "))
honor_lembur_per_jam = float(input("Masukkan honor lembur per jam: "))
jumlah_jam_lembur = float(input("Masukkan jumlah jam lembur: "))
jumlah_hari_kerja = int(input("Masukkan jumlah hari kerja: "))

# Menghitung total gaji karyawan
total_gaji = hitung_gaji(gaji_pokok, uang_transport_harian, uang_makan_harian, tunjangan_jabatan, honor_lembur_per_jam, jumlah_jam_lembur, jumlah_hari_kerja)

# Menampilkan total gaji karyawan
print("Total gaji karyawan adalah:", total_gaji)