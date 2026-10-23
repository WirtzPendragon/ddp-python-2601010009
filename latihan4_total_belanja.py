nama_barang = input("Masukkan nama barang: ")
harga_satuan = float(input("Masukkan harga satuan: "))
jumlah_barang = int(input("Masukkan jumlah barang: "))

subtotal = harga_satuan * jumlah_barang
ppn = subtotal * 0.11
total_belanja = subtotal + ppn

print(f"Nama Barang: {nama_barang}\nHarga Satuan: Rp{harga_satuan}\nJumlah Barang: {jumlah_barang}\nSubtotal: Rp{subtotal}\nPPN (11%): Rp{ppn}\nTotal Belanja: Rp{total_belanja}")