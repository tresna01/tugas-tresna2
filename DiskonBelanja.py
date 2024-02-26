uangBelanja = int(input("Masukkan uang belanja anda: "))
totalBelanja = int(input("Masukkan total belanja anda: "))

if totalBelanja > 70000:
    diskon = totalBelanja * (10/100)
else:
    diskon = 0;
    
print("anda mendapatkan diskon sebesar: %.0f" % diskon) 

totalKembalian = uangBelanja-totalBelanja+diskon

print("total kembalian anda adalah: %.0f" % totalKembalian)