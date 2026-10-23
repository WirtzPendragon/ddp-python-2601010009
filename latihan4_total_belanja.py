#Program menghitung total belanja dengan PPN 11%

#Mengambil input nama barang, harga satuan, dan jumlah barang dari user
nama_barang = input("Masukkan nama barang: ")
harga_satuan = float(input("Masukkan harga satuan: "))
jumlah_barang = int(input("Masukkan jumlah barang: "))

#Menghitung subtotal, PPN, dan total belanja
subtotal = harga_satuan * jumlah_barang
ppn = subtotal * 0.11
total_belanja = subtotal + ppn

#Menampilkan hasil perhitungan
print(f"Nama Barang: {nama_barang}\nHarga Satuan: Rp{harga_satuan}\nJumlah Barang: {jumlah_barang}\nSubtotal: Rp{subtotal}\nPPN (11%): Rp{ppn}\nTotal Belanja: Rp{total_belanja}")