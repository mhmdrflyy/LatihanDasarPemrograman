# tulis variabel harga barang 
# tulis variabel nama barang
# tulis variabel persen harga
# input nama barang
# input harga barang
# menghitung harga barang

while(True):
    harga_barang = int(input("Masukan harga barang : "))
    nama_barang = input("Masukan nama barang : ")
    persen = input("Masukan persen : ")
    harga_keuntungan = int(harga_barang) * int(persen) / 100
    harga_jual = int(harga_barang) + harga_keuntungan
    print(nama_barang, "dijual dengan : ", harga_jual)

    apakah_lanjut = input("apakah anda ingin melanjutkan? Y untuk Ya N untuk No : ")
    if(apakah_lanjut != "Y"):
        break