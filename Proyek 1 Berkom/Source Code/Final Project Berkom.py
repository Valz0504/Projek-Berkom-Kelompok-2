''' 
Author             : Kelompok 2
Nama Kelompok      :  - Ishaq Irfan Farizal (19624083)
                      - Fikrifalah Muslich  (19624086)
                      - Alya Nur Rahmah     (19624088)
                      - Safira Berlianti    (19624100)
                      - Emilio Justin       (19624137)
Tanggal Pengerjaan : 4-17 November 2024

---PROGRAM FOOD ORDERING SYSTEM COMPUTATIONAL SUSHI---
Deskripsi : Simulasi sistem pemesanan makanan di restoran secara sederhana

(KAMUS)
-int :
indeks_pesanan     : menyimpan sudah pesanan ke berapa dilakukan
max_pesanan        : menyimpan banyak maksimal pesanan dari berbagai menu yang berbeda
max_meja           : menyimpan banyak maksimal meja yang tersedia di restoran
antrian            : menyimpan nomor antrian dari pesanan yang sudah dipesan
Opsi               : menyimpan keputusan untuk Dine In atau Take Away
Nomor_meja         : menyimpan nomor meja yang sedang diduduki oleh pemesan
pilihan            : menyimpan nama varian manakan/minuman dari jenis menu (1-6)
banyak             : menyimpan banyak pesanan yang akan ditambahkan
harga              : mencatat harga dari pesanan yang kita pilih
choice_jenis       : menyimpan pilihan ke menu makanan/minuman yang ingin dipesan
choice_cek_pesanan : menyimpan keputusan untuk Tambah Pesanan atau Kurangi Pesanan
choice_bayar       : menyimpan pilihan jalur pembayaran
pilihan_kurang     : menyimpan pilihan pesanan yang ingin dikurangi
banyak_berkurang   : menyimpan banyak pesanan yang akan dikurangi
total_harga        : menyimpan total harga dari semua pesanan yang akan dipesan

-boolean :
mulai_pesan        : menyimpan boolean True/False untuk memulai pesanan (default : False)
pesan_lagi         : menyimpan boolean True/False untuk memesan lagi (default: True)
found              : menyimpan boolean True/False untuk mengecek ada kesamaan nama dari pesanan atau tidak (default : False)
back_page          : menyimpan boolean True/False untuk menu kembali ke halaman sebelumnya (default : False)
stok_tersedia      : menyimpan boolean True/False untuk mengecek persediaan stok dari produk yang dijual (default : True)
cek_pesanan        : menyimpan boolean True/False untuk menampilkan pesanan saat ini dan opsi yang tersedia di menunya (default : True)

-str :
jadi_pesan            : menyimpan konfirmasi memulai pesanan atau tidak
Nama_pemesan          : menyimpan nama pemesan
stok                  : menyimpan apakah stok dari produk tersedia atau tidak
item                  : menyimpan nama barang yang telah dipilih untuk dipesan
go_back_page          : menyimpan keputusan untuk kembali ke halaman utama atau tidak
nambah_pesanan        : menyimpan keputusan untuk menambah pesanan atau tidak
item_kurang           : menyimpan nama barang yang akan dikurangi jumlah pesanannya
opsi_pembayaran       : menyimpan jenis-jenis pembayaran yang tersedia
konfirmasi_pembayaran : menyimpan keputusan apakah sudah bayar atau tidak
yakin_batal           : menyimpan keputusan pembatalan pesanan
yakin_checkout        : menyimpan keputusan checkout

'''

#Modules untuk memperbagus visualisasi terminal
import os
import time

#VARIABEL DATA MENU --> Berisi variabel dan array tentang nama, harga, dan stok produk yang dijual
#=====================================================================================
sushi = 20
list_Sushi = ["Spicy Salmon Sushi", "Black Pepper Tuna Sushi", "Chicken Nanban Roll", "Maguro Tataki", "Chikuwa Cheese Roll", "Salmon Tempura Floss Roll"
              , "Kani Mayo Mentai Roll", "Oase Roll", "Veggie Roll", "Crispy Unagi Roll", "Tamago Maki", "Tuna Salad Maki,"
              , "Beef Tamago Cheese Maki", "Corn Cheese Maki", "Kani Mentai Sushi", "Salmon Mentai Sushi", "Unagi Sushi", "Tamago Sushi"
              , "Tamago Sushi", "Salmon Cheese Roll"]
stok_sushi = [100 for i in range(sushi)]
harga_Sushi = [27500, 16500, 44000, 27500, 44000, 44000, 33000, 33000, 33000, 22000, 55000, 22000, 33000, 55000, 11000,
               16500, 27500, 27500, 11000, 55000]

ramen = 5
list_Ramen = ["Shoyu Ramen", "Spicy Miso Ramen", "Grilled Chicken Ramen", "Chicken Katsu Ramen", "Goma Kara Ramen"]
stok_ramen = [100 for i in range(ramen)]
harga_Ramen = [22000, 22000, 48000, 50000, 49500]

ricebowl = 11
list_Ricebowl = ["Chicken Karaage Don", "Crispy Salmon Mentai Don", "Yakiniku Don", "Chicken Teriyaki Don", "Spicy Ten Don"
                 , "Chicken Karaage Mentai Rice", "Beef Teriyaki Mentai Rice", "Salmon Karaage Mentai Rice", "Cheese Katsu Don"
                 , "Chicken Nanban Don", "Salmon Tartar Don"]
stok_ricebowl = [100 for i in range(ricebowl)]
harga_Ricebowl = [22000, 27500, 27500, 22000, 27500, 27500, 27500, 27500, 22000, 27500, 27500]

minuman = 7
list_Minuman = ["Ocha", "Ice Tea", "Lemon Tea", "Iced Sweet Lychee Tea", "Iced Mango Tea","Iced Passion Fruit Tea", "Lemongrass Lychee Tea"]
stok_minuman = [100 for i in range(minuman)]
harga_Minuman = [8000, 7000, 10000, 25000, 25000, 25000, 20000]

PaketWibu = 2
list_PaketWibu = ["PaketWibu A", "PaketWibu B"]
stok_PaketWibu = [100 for i in range(PaketWibu)]
harga_PaketWibu = [50000, 55000]

Appetizer = 6
list_Appetizer = ["Cheese Dorayaki", "Chocolate Dorayaki", "Strawberry Choux", "Mix Dorayaki", "Matcha Choux", "Chocolate Choux"]
stok_Appetizer = [100 for i in range(Appetizer)]
harga_Appetizer = [16500, 16500, 17000, 16500, 17000, 17000]
#=====================================================================================


#VARIABEL DATA PESANAN --> Array yang mencatat pesanan/produk yang telah dipilih
#=================================
max_pesanan = 100
indeks_pesanan = 0
pesanan_nama = [""] * max_pesanan
pesanan_jumlah = [0] * max_pesanan
pesanan_harga = [0] * max_pesanan
pesanan_total = [0] * max_pesanan
total_harga = 0
kustomisasi = [""] * max_pesanan
#=================================

#Variabel Data Meja dan Nomor Antrian
max_meja = 20
antrian = 1

#Fungsi yang mengecek stok sushi
def cek_stok(list_barang, stok_barang, harga_barang, jenis_menu):
    for i in range(jenis_menu):
        stok_tersedia = True
        if stok_barang[i] <= 0:
            stok_tersedia = False
        
        if stok_tersedia:
            stok = "Tersedia"
        else:
            stok = "Habis"
        print(f"{i+1}. {list_barang[i]}" + " "*(40 - len(list_barang[i] + f"{i + 1}"))  + f"Rp. {harga_barang[i]}     -{stok}({stok_barang[i]})-")

#Fungsi yang mencatat dan mengecek pesanan yang dipilih dan mengembalikan indeks_pesanan yang sudah diupdate
def mengecek_pesanan(list_barang, harga_barang, indeks_pesanan, pilihan, banyak, pesanan_nama, pesanan_jumlah, pesanan_harga, pesanan_total):
    
    item = list_barang[pilihan - 1]
    harga = harga_barang[pilihan - 1]

    found = False
    for i in range(indeks_pesanan):
        if pesanan_nama[i] == item:
            pesanan_jumlah[i] += banyak
            pesanan_total[i] += banyak * harga
            found = True
    if found == False:
        pesanan_nama[indeks_pesanan] = item
        pesanan_jumlah[indeks_pesanan] = banyak
        pesanan_harga[indeks_pesanan] = harga
        pesanan_total[indeks_pesanan] = banyak * harga
        indeks_pesanan += 1
    
    return indeks_pesanan

#Fungsi Mengurangi Stok
def kurangi_stok(stok_barang, pilihan, banyak):

    stok_barang[pilihan-1] -= banyak
    if (stok_barang[pilihan-1] <= 0):
        stok_barang[pilihan-1] = 0

#Fungsi Kembali ke halaman utama / tambah pesanan
def kembali_ke_halaman():
    back_page = False
    while back_page == False:
        go_back_page = input("Kembali ke halaman daftar jenis pesanan? (y/n): ")
        if (go_back_page == 'n'):
            nambah_pesanan = input("Tambah pesanan? (y/n): ")
            print()
            if (nambah_pesanan == 'n'):
                pesan_lagi = False
            elif (nambah_pesanan == 'y'):
                os.system('cls')
                back_page = True
                pesan_lagi = True
        elif (go_back_page == 'y'):
            os.system('cls')
            back_page = True
            pesan_lagi = False
    return pesan_lagi

#Fungsi gabungan untuk pemilihan menu, banyak, mengecek pesanan, dan menambah pesanan
def do_order(list_barang, stok_barang, harga_barang, indeks_pesanan, choice_jenis, total_harga):

    #Inisialiasi return value yang akan dikembalikan oleh fungsi ini, digunakan array karena akan ada 2 value yang ingin dikembalikan
    return_value = [0,0]

    #Memilih pilihan menu dan menentukan jumlahnya
    while True:
        pilihan = input("Pilih nomor: ")
        if pilihan != "":
            pilihan = int(pilihan)
            if pilihan > 0 and pilihan < len(list_barang)+1:
                if stok_sushi[pilihan-1] > 0:
                    break
                else:
                    print(f"Maaf, stok {list_barang[pilihan-1]} habis. Silakan pilih menu yang lain")
            else:
                print('Pastikan angka yang Anda masukkan benar.')

    while True:
        banyak = input("Banyak: ")
        if banyak != "":
            banyak = int(banyak)
            if banyak <= stok_barang[pilihan-1] and banyak > 0:
                break
            else:
                print("Melebihi stok")
    print()

    #Mengupdate indeks_pesanan jika pesanan sudah ditambahkan
    indeks_pesanan = mengecek_pesanan(list_barang, harga_barang,indeks_pesanan, pilihan, banyak, pesanan_nama, pesanan_jumlah, pesanan_harga, pesanan_total)
    
    #Mengurangi stok sesuai dengan jumlah pesanan yang sudah ditambahkan ke daftar pesanan
    kurangi_stok(stok_barang, pilihan, banyak)

    #Memberi keterangan untuk tambahan
    kustomisasi[indeks_pesanan-1] = input("Masukkan keterangan untuk tambahan untuk makanan/minuman: ")

    return_value[0] = indeks_pesanan
    return_value[1] = total_harga

    return return_value



#ALGORITMA PROGRAM
while True:
    mulai_pesan = False
    while (mulai_pesan == False):

        #TAMPILAN DEPAN
        print(" _____________________________________________________________")
        print("|                Welcome to Computational Sushi               |")
        print("|                                                             |")
        print("|                                                             |")
        print("|   Restoran kami menyediakan berbagai menu asli dari Jepang  |")
        print("|           dengan kualitas bahan yang paling tinggi.         |")
        print("|                                                             |")
        print("|_____________________________________________________________|")
        jadi_pesan = input("Mulai pesen? (y/n): ")
        if (jadi_pesan == "y"):
            mulai_pesan = True

            time.sleep(0.3)
            os.system('cls')

        else:

            time.sleep(0.3)
            os.system('cls')

    #ISI IDENTITAS
    Nama_pemesan = ""
    while Nama_pemesan == "":
        print("---CUSTOMER INFORMATION---")
        Nama_pemesan = input("Masukkan nama kamu: ")

        if (Nama_pemesan != ""):
            break
        else:
            os.system('cls')

    #Pemilihan Dine In/Take Away
    Opsi = 0
    while Opsi != 1 or Opsi != 2:

        Opsi = input("Dine In / Take Away? (1/2): ")
        if (Opsi != ""):
            Opsi = int(Opsi)

            if Opsi == 1:
                Nomor_meja = 0
                while True:
                    Nomor_meja = input("Masukkan nomor meja yang kamu duduki: ")
                    if (Nomor_meja != ""):
                        Nomor_meja = int(Nomor_meja)
                        if Nomor_meja <= max_meja:
                            break
                        else:
                            print("Pastikan nomor meja yang Anda masukkan benar dan sesuai")
                break

            elif Opsi == 2:
                break

    time.sleep(0.3)
    os.system('cls')
    
    choice_jenis = 0
    while (mulai_pesan == True):
        #LIST JENIS MAKANAN
        print(" ________________________ ")
        print("|Daftar Jenis Pesanan:   |")
        print("|1. Sushi                |")
        print("|2. Ramen                |")
        print("|3. Rice Bowl            |")
        print("|4. Minuman              |")
        print("|5. Paket Wibu           |")
        print("|6. Appetizer            |")
        print("|________________________|")
        print("|7. Cek Pesanan          |")
        print("|8. Batal Pesan          |")
        print("|________________________|")

        while True:
            choice_jenis = input("Opsi: ")
            if (choice_jenis != ""):
                choice_jenis = int(choice_jenis)
                time.sleep(0.5)

                os.system('cls')
                break

        if (choice_jenis > 0 and choice_jenis <= 8):

            #Pemilihan Sushi
            if (choice_jenis == 1):
                pesan_lagi = True

                while pesan_lagi:
                    print('Masukkan angka yang sesuai dengan nomor dipilihan.')
                    print("Pilihan Sushi:")
                    print()
                    
                    #Mengecek ketersediaan stok terlebih dahulu
                    cek_stok(list_Sushi, stok_sushi, harga_Sushi, sushi)

                    #Fungsi do_order() akan dijalankan dengan beberapa algoritma di dalamnya dan mengembalikan "indeks_pesanan" yang telah diupdate
                    indeks_dan_totalharga = do_order(list_Sushi, stok_sushi, harga_Sushi, indeks_pesanan, choice_jenis, total_harga)

                    indeks_pesanan = indeks_dan_totalharga[0]
                    total_harga = indeks_dan_totalharga[1]

                    #Fungsi opsi kembali ke halaman utama / tambah pesanan
                    pesan_lagi = kembali_ke_halaman()  

            #Pemilihan Ramen
            elif (choice_jenis == 2):
                pesan_lagi = True

                while pesan_lagi:
                    print('Masukkan angka yang sesuai dengan nomor dipilihan.')
                    print("Pilihan Ramen: ")
                    print()

                    #Mengecek ketersediaan stok terlebih dahulu
                    cek_stok(list_Ramen, stok_ramen, harga_Ramen, ramen)

                    #Fungsi do_order() akan dijalankan dengan beberapa algoritma di dalamnya dan mengembalikan "indeks_pesanan" yang telah diupdate
                    indeks_dan_totalharga = do_order(list_Ramen, stok_ramen, harga_Ramen, indeks_pesanan, choice_jenis, total_harga)

                    indeks_pesanan = indeks_dan_totalharga[0]
                    total_harga = indeks_dan_totalharga[1]

                    #Fungsi opsi kembali ke halaman utama / tambah pesanan
                    pesan_lagi = kembali_ke_halaman() 

            #Pemilihan Ricebowl
            elif (choice_jenis == 3):
                pesan_lagi = True

                while pesan_lagi:
                    print('Masukkan angka yang sesuai dengan nomor dipilihan.')
                    print("Pilihan Ricebowl:")
                    print()

                    #Mengecek ketersediaan stok terlebih dahulu
                    cek_stok(list_Ricebowl, stok_ricebowl, harga_Ricebowl, ricebowl)

                    #Fungsi do_order() akan dijalankan dengan beberapa algoritma di dalamnya dan mengembalikan "indeks_pesanan" yang telah diupdate
                    indeks_dan_totalharga = do_order(list_Ricebowl, stok_ricebowl, harga_Ricebowl, indeks_pesanan, choice_jenis, total_harga)

                    indeks_pesanan = indeks_dan_totalharga[0]
                    total_harga = indeks_dan_totalharga[1]

                    #Fungsi opsi kembali ke halaman utama / tambah pesanan
                    pesan_lagi = kembali_ke_halaman() 

            #Pemilihan Minuman
            elif (choice_jenis == 4):
                pesan_lagi = True

                while pesan_lagi:
                    print('Masukkan angka yang sesuai dengan nomor dipilihan.')
                    print("Pilihan Minuman: ")
                    print()

                    #Mengecek ketersediaan stok terlebih dahulu
                    cek_stok(list_Minuman, stok_minuman, harga_Minuman, minuman)

                    #Fungsi do_order() akan dijalankan dengan beberapa algoritma di dalamnya dan mengembalikan "indeks_pesanan" yang telah diupdate
                    indeks_dan_totalharga = do_order(list_Minuman, stok_minuman, harga_Minuman, indeks_pesanan, choice_jenis, total_harga)

                    indeks_pesanan = indeks_dan_totalharga[0]
                    total_harga = indeks_dan_totalharga[1]

                    #Fungsi opsi kembali ke halaman utama / tambah pesanan
                    pesan_lagi = kembali_ke_halaman() 

            #Pemilihan PaketWibu
            elif (choice_jenis == 5):
                pesan_lagi = True

                while pesan_lagi:
                    print('Masukkan angka yang sesuai dengan nomor dipilihan.')
                    print("Pilihan PaketWibu")
                    print()

                    #Mengecek ketersediaan stok terlebih dahulu
                    cek_stok(list_PaketWibu, stok_PaketWibu, harga_PaketWibu, PaketWibu)

                    #Fungsi do_order() akan dijalankan dengan beberapa algoritma di dalamnya dan mengembalikan "indeks_pesanan" yang telah diupdate
                    indeks_dan_totalharga = do_order(list_PaketWibu, stok_PaketWibu, harga_PaketWibu, indeks_pesanan, choice_jenis, total_harga)

                    indeks_pesanan = indeks_dan_totalharga[0]
                    total_harga = indeks_dan_totalharga[1]

                    #Fungsi opsi kembali ke halaman utama / tambah pesanan
                    pesan_lagi = kembali_ke_halaman() 

            #Pemilihan Appetizer
            elif (choice_jenis == 6):
                pesan_lagi = True

                while pesan_lagi:
                    print('Masukkan angka yang sesuai dengan nomor dipilihan.')
                    print("Pilihan appetizer:")
                    print()

                    #Mengecek ketersediaan stok terlebih dahulu
                    cek_stok(list_Appetizer, stok_Appetizer, harga_Appetizer, Appetizer)

                    #Fungsi do_order() akan dijalankan dengan beberapa algoritma di dalamnya dan mengembalikan "indeks_pesanan" yang telah diupdate
                    indeks_dan_totalharga = do_order(list_Appetizer, stok_Appetizer, harga_Appetizer, indeks_pesanan, choice_jenis, total_harga)

                    indeks_pesanan = indeks_dan_totalharga[0]
                    total_harga = indeks_dan_totalharga[1]

                    #Fungsi opsi kembali ke halaman utama / tambah pesanan
                    pesan_lagi = kembali_ke_halaman() 

            #Cek Pesanan
            elif (choice_jenis == 7):

                if indeks_pesanan != 0:
                    cek_pesanan = True

                    #Menampilkan pesanan saat ini dan memberi opsi Kembali / Kurangi pesanan / Checkout
                    while cek_pesanan:
                        print("Pesanan saat ini: ")
                        if indeks_pesanan != 0:
                            for i in range(indeks_pesanan):
                                print(f"{i+1}. {pesanan_nama[i]}: {pesanan_jumlah[i]}")
                        else:
                            print("-")
                        print()
                        print("Opsi: ")
                        print("1. Kurangi pesanan")
                        print("2. Kembali ke halaman daftar jenis pesanan")
                        print("3. Checkout")

                        while True:
                            choice_cek_pesanan = input("Pilih opsi: ")
                            if choice_cek_pesanan != "":
                                choice_cek_pesanan = int(choice_cek_pesanan)
                                break
                        print()

                        #Kembali ke halaman Daftar Jenis Makanan
                        if choice_cek_pesanan == 2:
                            print("Kembali ke halaman Daftar Jenis Pesanan. . .")
                            time.sleep(1)

                            os.system('cls')

                            cek_pesanan = False
                            pesan_lagi = False

                        #Mengurangi pesanan
                        elif choice_cek_pesanan == 1:

                            if indeks_pesanan != 0:
                                while True:
                                    pilihan_kurang = input("Pilih pesanan yang mau dikurangi: ")
                                    
                                    if pilihan_kurang != "":
                                        pilihan_kurang = int(pilihan_kurang)
                                        if pilihan_kurang > 0 and pilihan_kurang <= indeks_pesanan:
                                            break
                                        else:
                                            print("Masukkan angka yang sesuai")
                                while True:
                                    banyak_berkurang = input("Banyak pesanan yang dikurang: ")
                                    
                                    if banyak_berkurang != "":
                                        banyak_berkurang = int(banyak_berkurang)
                                        if banyak_berkurang > 0 and banyak_berkurang <= pesanan_jumlah[pilihan_kurang-1]:
                                            time.sleep(0.5)
                                            
                                            os.system('cls')
                                            break
                                        else:
                                            print("Masukkan banyak yang sesuai")

                                item_kurang = pesanan_nama[pilihan_kurang-1]
                                for i in range(indeks_pesanan):
                                    if item_kurang == pesanan_nama[i]:
                                        if pesanan_jumlah[i] > 0:
                                            pesanan_jumlah[i] -= banyak_berkurang
                                            pesanan_total[i] -= banyak_berkurang * pesanan_harga[i]
                                            if pesanan_jumlah[i] <= 0:
                                                pesanan_nama[i] = ""
                                                pesanan_harga[i] = 0
                                                pesanan_total[i] = 0
                                                for j in range(i, indeks_pesanan+1):
                                                    pesanan_nama[j] = pesanan_nama[j+1]
                                                    pesanan_harga[j] = pesanan_harga[j+1]
                                                    pesanan_jumlah[j] = pesanan_jumlah[j+1]
                                                    pesanan_total[j] = pesanan_total[j+1]
                                                indeks_pesanan -= 1

                                #Mengembalikan stok apabila ada menu yang dikurangi
                                for i in range (sushi):
                                    if list_Sushi[i]==item_kurang:
                                        stok_sushi[i]+=banyak_berkurang
                                for i in range (ramen):
                                    if list_Ramen[i]==item_kurang:
                                        stok_ramen[i]+=banyak_berkurang
                                for i in range (ricebowl):
                                    if list_Ricebowl[i]==item_kurang:
                                        stok_ricebowl[i]+=banyak_berkurang
                                for i in range (minuman):
                                    if list_Minuman[i]==item_kurang:
                                        stok_minuman[i]+=banyak_berkurang
                                for i in range (PaketWibu):
                                    if list_PaketWibu[i]==item_kurang:
                                        stok_PaketWibu[i]+=banyak_berkurang
                                for i in range (Appetizer):
                                    if list_Appetizer[i]==item_kurang:
                                        stok_Appetizer[i]+=banyak_berkurang
                        
                            else: 
                                print("Pesanan anda kosong, tidak dapat mengurangi pesanan")
                                time.sleep(2)

                                os.system('cls')  
                            print()

                        #Checkout
                        elif choice_cek_pesanan == 3:
                            if indeks_pesanan != 0:
                                #HARGA AKHIR
                                for i in range(max_pesanan):
                                    total_harga += pesanan_total[i]

                                #Konfirmasi checkout
                                yakin_mau_checkout = True
                                while yakin_mau_checkout:
                                    yakin_checkout = input("Apakah yakin untuk checkout? (y/n): ")
                                    if (yakin_checkout == "y"):
                                        time.sleep(1)
                                        os.system('cls')
                                        print("Tip anda akan sangat berarti untuk kami")
                                        tip = int(input("Rp. "))
                                        total_harga += tip

                                        #OPSI PEMBAYARAN
                                        opsi_pembayaran = ["Tunai", "ATM", "Kredit", "QRIS"]
                                        print("Opsi pembayaran: ")
                                        for i in range(4):
                                            print(f"{i+1}. {opsi_pembayaran[i]}")

                                        while True:
                                            choice_bayar = input("Pilih pembayaran: ")
                                            if choice_bayar != "":
                                                choice_bayar = int(choice_bayar)
                                                if (choice_bayar <= 0 or choice_bayar > 4):
                                                    print("Pastikan pilihan Anda sesuai.")
                                                else:
                                                    break

                                        #PENCETAKAN STRUK PESANAN
                                        print("Struk pesananmu sedang dicetak. . . ")
                                        time.sleep(3)
                                        os.system('cls')

                                        #STRUK PESANAN
                                        if choice_bayar != 4:  #Selain QRIS
                                            print("___________________________________________________")
                                            print("STRUK PESANAN                                         ")
                                            print()
                                            print(f"Nama: {Nama_pemesan}                              ")
                                            print(f"Nomor Antrian: {antrian}")
                                            print("--------------------------------------------------")
                                            if (Opsi == 1):
                                                print("                     DINE IN                        ")
                                                print(f"Nomor Meja: {Nomor_meja}                                     ")
                                            else:
                                                print("                     TAKE AWAY                       ")
                                            print("--------------------------------------------------")
                                            for i in range(indeks_pesanan):
                                                print(f"{pesanan_nama[i]}: {pesanan_jumlah[i]} x Rp.{pesanan_harga[i]} : Rp.{pesanan_total[i]}")
                                                print(f"Keterangan pesanan: {kustomisasi[i]}")
                                            print(f"Tip : {tip}")
                                            print(f"Total Harga: Rp{total_harga}                              ")
                                            print(f"Pembayaran: {opsi_pembayaran[choice_bayar-1]}")
                                            print("Silakan lakukan pembayaran di KASIR, terima kasih.")
                                            print("___________________________________________________")

                                            time.sleep(7)

                                            antrian += 1
                                            cek_pesanan = False
                                            mulai_pesan = False
                                            
                                            os.system('cls')
                                            break

                                        else:
                                            while True:   #QRIS
                                                print("___________________________________________________")
                                                print("STRUK PESANAN                                         ")
                                                print()
                                                print(f"Nama: {Nama_pemesan}                              ")
                                                print(f"Nomor Antrian: {antrian}")
                                                print("--------------------------------------------------")
                                                if (Opsi == 1):
                                                    print("                     DINE IN                        ")
                                                    print(f"Nomor Meja: {Nomor_meja}                                     ")
                                                else:
                                                    print("                     TAKE AWAY                       ")
                                                print("--------------------------------------------------")
                                                for i in range(indeks_pesanan):
                                                    print(
                                                        f"{pesanan_nama[i]}: {pesanan_jumlah[i]} x Rp.{pesanan_harga[i]} : Rp.{pesanan_total[i]}")
                                                print(f"Tip : Rp. {tip}")
                                                print(f"Total Harga: Rp{total_harga}                              ")
                                                print(f"Pembayaran: {opsi_pembayaran[choice_bayar - 1]}")
                                                print("Silakan melakukan pembayaran langsung")
                                                print('''
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@                 @@@@@@@/  @@*  @@@@@@@.  @@@@@  @@@@@                 ,@@@
@@@  @@@@@@@@@@@@%  @@#  @@(  @@@@@               @@   @@   @@@@@@@@@@@@  ,@@@
@@@  @@@       @@%  @@@@@@@@@@@@*  @@@@@     @@@@@     @@   @@        @@  ,@@@
@@@  @@@       @@%  @@#       @@/    #@@  %@@     @@   @@   @@        @@  ,@@@
@@@  @@@       @@%  @@@@@  /@@@@@@@     @@,         @@@@@   @@       .@@  ,@@@
@@@  @@@@@@@@@@@@%  @@#    /@@     @@@@@  %@@@@@@@@@@@@@@   @@@@@@@@@@@@  ,@@@
@@@                 @@#  @@/  @@*  @@,  @@.  @@.  @@   @@                 ,@@@
@@@@@@@@@@@@@@@@@@@@@@@@@       (@@@@,  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@            @@%         (@@       %@@  %@@     @@     @@@  @@@  @@&  @@@@@@
@@@@@   @@  .@@  ,@@     @@/  @@/  @@,  @@.  @@@@@  @@@          @@@@@@@  ,@@@
@@@@@   @@     @@%  @@#  @@/  @@@@@          @@@@@@@@@@  @@@@@@@@@@   @@@@@@@@
@@@@@@@@         ,@@  *@@@@@@@@@@@@@@&###### @@.    @@@            @@@@@@@@@@@
@@@  @@@       @@%              @           @     @@@@@  @@@@@@@@  @@&  @@@@@@
@@@  @@@  @@@@@@@@@@@@@@@  /@@  @           @@@@@@     @@             @@  ,@@@
@@@     @@   @@@@%  @@@@@  (@@@@@           @@@.  @@        @@@@@    .@@@@@@@@
@@@@@   @@       ,@@  *@@       @           @@@@@@@@     @@@       @@&    ,@@@
@@@     @@@@@         /@@  (@@@@@@/////////#@       @@@  @@@  @@@@@     @@@@@@
@@@       @@@@@@@@@@     @@(       @@*  @@@@@  &@@  @@@@@   @@   @@       ,@@@
@@@  @@@@@@@@@@     @@@@@@@@@@@@@@@@@@@@  %@@@@.  @@   @@@@@@@@@@  @@&  @@@@@@
@@@  @@@  @@@@@@@@@@  *@@  (@@@@@@@@@@@@     @@.  @@@@@     @@     @@@@@  ,@@@
@@@  @@@@@@@&  @@%            @@@@@  #@@                         @@       ,@@@
@@@@@@@@@@@@@@@@@@@@@@#  @@@@@     @@,  @@@@@@@@@@     @@@@@@@     @@@@@  ,@@@
@@@                 @@#  @@@@@@@/    #@@     @@.       @@   @@   @@@@@@@@@@@@@
@@@  @@@@@@@@@@@@%  @@@@@  (@@@@@@@@@*  @@@@@@@.  @@   @@@@@@@   @@@@&  @@@@@@
@@@  @@@       @@%  @@#       @@@@@  #@&          @@            .@@     @@&@@@
@@@  @@@       @@%  @@#  @@@@@     @@,  @@@@@       @@@@@@@@@@@@@@@@@@@@  ,@@@
@@@  @@&       @@%  @@#    (@@@@@@@@@*    %@@@@@@@@@@@@     @@. .@@  .  @@@@@@
@@@  @@@@@@@@@@@@%  @@#  @@/       @@@@&  %@@@@@@@@@     &@@@@@@@@@@@&  @@@@@@
@@@                 @@#  @@(  @@/       @@,         @@@     @@@@@    ,@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                            ''')
                                                print("___________________________________________________")
                                                print()

                                                #Konfirmasi Pembayaran
                                                while True:
                                                    konfirmasi_pembayaran = input("Konfirmasi pembayaran (y/n): ")
                                                    if konfirmasi_pembayaran != "":
                                                        break

                                                if konfirmasi_pembayaran == 'y':
                                                    print("Terima kasih sudah melakukan pembayaran, pesanan segera disiapkan, mohon ditunggu.")
                                                    time.sleep(4)

                                                    antrian += 1
                                                    cek_pesanan = False
                                                    mulai_pesan = False
                                                    yakin_mau_checkout = False

                                                    os.system('cls')
                                                    break

                                                elif konfirmasi_pembayaran == 'n':
                                                    print("Maaf pembayaran belum berhasil. Silakan coba lagi.")
                                                    time.sleep(2)
                                                    
                                                    os.system('cls')

                                    elif yakin_checkout == "n":

                                        os.system('cls')

                                        print("Kembali ke halaman cek pesanan. . .")
                                        time.sleep(1)

                                        os.system('cls')

                                        pesan_lagi = False
                                        break
                            else:
                                print("Pesanan anda kosong, tidak dapat melakukan checkout")

                                time.sleep(2)
                                os.system('cls')  

                else:
                    print("Maaf kamu belum melakukan pesanan, kami akan alihkan ke daftar jenis pesanan. . .")
                    time.sleep(3)

                    os.system('cls')

                    pesan_lagi = False


            #Batal Pesan
            elif (choice_jenis == 8):
                while True:
                    yakin_batal = input("Apakah yakin untuk membatalkan pesanan? (y/n): ")
                    if yakin_batal == 'y':
                        print("Pesanan dibatalkan, beralih ke halaman utama. . .")
                        time.sleep(1.5)

                        os.system('cls')
                        mulai_pesan = False

                        #Mengembalikan stok apabila pesanan dibatalkan
                        for i in range (indeks_pesanan):
                            for j in range (sushi):
                                if list_Sushi[j]==pesanan_nama[i]:
                                    stok_sushi[j]+=pesanan_jumlah[i]
                            for j in range (ramen):
                                if list_Ramen[j]==pesanan_nama[i]:
                                    stok_ramen[j]+=pesanan_jumlah[i]
                            for j in range (ricebowl):
                                if list_Ricebowl[j]==pesanan_nama[i]:
                                    stok_ricebowl[j]+=pesanan_jumlah[i]
                            for j in range (minuman):
                                if list_Minuman[j]==pesanan_nama[i]:
                                    stok_minuman[j]+=pesanan_jumlah[i]
                            for j in range (PaketWibu):
                                if list_PaketWibu[j]==pesanan_nama[i]:
                                    stok_PaketWibu[j]+=pesanan_jumlah[i]
                            for j in range (Appetizer):
                                if list_Appetizer[j]==pesanan_nama[i]:
                                    stok_Appetizer[j]+=pesanan_jumlah[i]
                        break
                    elif yakin_batal == 'n':
                        time.sleep(0.5)

                        os.system('cls')

                        pesan_lagi = False
                        break

        else:  #Jika pada opsi pilihan daftar jenis makanan, user tidak memasukkan angka yang pas
            print("Pastikan angka Anda sesuai.")
