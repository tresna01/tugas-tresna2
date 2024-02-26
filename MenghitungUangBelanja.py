#Daftar Buah Buhan per-kilo
jeruk = 3
apel = 2
mangga = 0
manggis = 5
durian = 2

# Harga Buah Per-kilo
harga_jeruk = 15.000
harga_apel = 30.000
harga_mangga = 20.000
harga_manggis = 7.000
harga_durian = 50.000

total_jeruk = jeruk * harga_jeruk
total_apel = apel * harga_apel
total_mangga = mangga * harga_mangga
total_manggis = manggis * harga_manggis
total_durian = durian * harga_durian

total_belanja = (total_jeruk + total_apel + total_mangga + total_manggis + total_durian)

print("Total yang harus kamu bayar adalah")
print (f"{jeruk} kilo jeruk = {total_jeruk}")
print (f"{apel} kilo jeruk = {total_apel}")
print (f"{mangga} kilo jeruk = {total_mangga}")
print (f"{manggis} kilo jeruk = {total_manggis}")
print (f"{durian} kilo jeruk = {total_durian}")
print("total belanja %.0f" % total_belanja)