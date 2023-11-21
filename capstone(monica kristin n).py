list_iphone = [
    {
     "kode barang" : "11/64gb/hitam",
     "tipe" : "Iphone 11",
     "stock" : 3,
     "harga" : 7499000,
     "kapasitas" : "64 gb",
     "warna" : "Hitam"
     },
    {
     "kode barang" : "11/128gb/putih",
     "tipe" : "Iphone 11",
     "stock" : 10,
     "harga" : 899000,
     "kapasitas" : "128 gb",
     "warna" : "Putih"
     },
    #  {
    #  "kode barang" : "12/64gb/ungu",
    #  "tipe" : "Iphone 12",
    #  "stock" : 5,
    #  "harga" : 9999000,
    #  "kapasitas" : "64 gb",
    #  "warna" : "Ungu"
    #  },
    #  { 
    #  "kode barang" : "12/128gb/merah",
    #  "tipe" : "Iphone 12",
    #  "stock" : 6,
    #  "harga" : 10999000,
    #  "kapasitas" : "128 gb",
    #  "warna" : "Merah"
    #  },
    #  { 
    #  "kode barang" : "12/128gb/hitam",
    #  "tipe" : "Iphone 12",
    #  "stock" : 17,
    #  "harga" : 10999000,
    #  "kapasitas" : "128 gb",
    #  "warna" : "Hitam"
    #  },
    #  {
    #  "kode barang" : "13/128gb/midnight",
    #  "tipe" : "Iphone 13",
    #  "stock" : 20,
    #  "harga" : 11999000,
    #  "kapasitas" : "128 gb",
    #  "warna" : "Midnight"
    #  },
    #  {
    #  "kode barang" : "13/256gb/pink",
    #  "tipe" : "Iphone 13",
    #  "stock" : 15,
    #  "harga" : 14499000,
    #  "kapasitas" : "256 gb",
    #  "warna" : "Pink"
    #  },
    #  {
    #  "kode barang" : "13/512gb/biru",
    #  "tipe" : "Iphone 13",
    #  "stock" : 19,
    #  "harga" : 15499000,
    #  "kapasitas" : "512 gb",
    #  "warna" : "Biru"
    #  },
    #  {
    #  "kode barang" : "14/256gb/ungu",
    #  "tipe" : "Iphone 14",
    #  "stock" : 21,
    #  "harga" : 16499000,
    #  "kapasitas" : "256 gb",
    #  "warna" : "Ungu"
    #  },
    # {
    #  "kode barang" : "14pro/128gb/silver",
    #  "tipe" : "Iphone 14 Pro",
    #  "stock" : 15,
    #  "harga" : 17599000,
    #  "kapasitas" : "128 gb",
    #  "warna" : "Silver"
    #  }
    ]

def menampilkan_daftar_produk() :
    if not list_iphone:
        print("\n\n Maaf produk Iphone habis, tidak ada tampilan produk apapun.")
    elif(pilih_menu == "1"):
        while True:
            pilihan_user= input('''
----------------------------------------
***********DAFTAR PRODUK KAMI***********
----------------------------------------  
                                        
    1.Tampilkan Seluruh Produk
    2.Tampilkan Produk Tertentu
    3.Kembali ke Menu Utama

Pilih Produk yang kamu cari [1-3]: ''')
    
            if(pilihan_user == "1"):
                judul = "Daftar Produk".center(90," ")
                print(judul)
                print("\n\n|Kode Barang\t\t|Tipe Iphone\t|Stock\t|Harga\t\t|Kapasitas\t|Warna")
                for i in range(len(list_iphone)):
                    print("|{:<16}\t| {:<12}\t| {:<6}| {:<9}\t| {:<12}\t| {:<8}".format(list_iphone[i]["kode barang"],list_iphone[i]["tipe"],list_iphone[i]["stock"],list_iphone[i]["harga"],list_iphone[i]["kapasitas"],list_iphone[i]["warna"]))
   
            elif(pilihan_user == "2"):
                    kode_barang = input('''
Input Kode Barang Iphone dengan format,
[tipe HP brp/kapasitas RAM/warna] contohnya 11/64gb/hitam
jika iphone pro formatnya 14pro/256gb/hitam : ''')
                    kode_barang = kode_barang.lower()
                    found = False
                    for product in list_iphone:
                        if kode_barang.lower() == product["kode barang"]:
                            found = True
                            print("\n\n| Kode Barang\t\t| Tipe Iphone\t| Stock\t| Harga\t\t| Kapasitas\t| Warna")
                            print("| {:<16}\t| {:<12}\t| {:<6}| {:<9}\t| {:<12}\t| {:<8}".format(product["kode barang"], product["tipe"], product["stock"], product["harga"], product["kapasitas"], product["warna"]))
                            break      
                    if not found:
                        print("\n\nProduk yang Anda cari tidak ditemukan.")



            elif(pilihan_user == "3"):
                break


def menambah_produk():
    while True:
        tambah_produk = input('''
----------------------------------------
***********MENAMBAHKAN PRODUK***********
----------------------------------------

1. Tambah Tipe Produk Iphone lainnya disini:
2. Kembali ke menu awal
                          
Silahkan input submenu yang akan dijalankan: ''')

        if tambah_produk == "1":
            kode_barang1 = input('''
Input Kode Produk Iphone dengan format,
[tipe HP brp/kapasitas RAM/warna] contohnya 11/64gb/hitam
jika iphone pro formatnya 14pro/256gb/hitam : ''')
            kode_barang1 = kode_barang1.lower()
            kode_ada = False

            for i in range(len(list_iphone)):
                if kode_barang1 == list_iphone[i]["kode barang"]:
                    kode_ada = True
                    print("\n\nTipe Produk yang Anda Input sudah ada")
                    break

            if not kode_ada:
                tipe1 = input("Input tipe contoh Iphone 12 : ")
                while True:
                    try:
                        stock1 = int(input("\nInput banyaknya stok Iphone : "))
                        break
                    except ValueError:
                        print("\nStock harus dalam bentuk angka.")
                while True:
                    try:
                        harga1 = int(input("\nInput harga Iphone: "))
                        break
                    except ValueError:
                        print("\nHarga harus dalam bentuk angka")
                        
                kapasitas1 = input("\nInput kapasitas Iphone berapa GB: ")
                warna1 = input("\nMasukkan warna Iphone: ")
                produk_baru ={
                    "kode barang": kode_barang1,
                    "tipe": tipe1,
                    "stock": stock1,
                    "harga": harga1,
                    "kapasitas": kapasitas1,
                    "warna": warna1,
                }
                list_iphone.append(produk_baru) 
                jawaban = input("Apakah Anda ingin menambahkan Produk ini {} yes/no ?: ".format(produk_baru))
                print("Tambahan Tipe Produk Kamu Berhasil Disimpan ")
                jawaban = jawaban.lower()
                if jawaban != "yes":
                    list_iphone.remove(produk_baru)
                    print("Tidak ada penambahan produk")
                    
                    
                else:
                    continue
                    


        elif tambah_produk == "2":
            break

       
              


def menghapus_produk():
    if not list_iphone:
        print("\n\n Maaf produk Iphone habis, tidak ada produk hrs dihapus.")
    else:
        while True:             
            hapus_produk = input('''
---------------------------------------
************MENGHAPUS PRODUK************
----------------------------------------

1. Hapus Tipe Produk Iphone disini:
2. Kembali ke menu awal
                          
Silahkan input submenu yang akan dijalankan: ''')         

            if hapus_produk == "1":
                hapus_produk_tertentu = input('''
Input Kode Produk Iphone yang akan dihapus dengan format,
[tipe HP brp/kapasitas RAM/warna] contohnya 11/64gb/hitam
jika iphone pro formatnya 14pro/256gb/hitam : ''')
                hapus_produk_tertentu = hapus_produk_tertentu.lower()
                produk_ditemukan = False

                i = 0
                while i < len(list_iphone):
                    if hapus_produk_tertentu == list_iphone[i]["kode barang"]:
                        produk_ditemukan = True     
                        jawaban1 = input("Apakah Kamu Yakin akan Menghapus Produk {} ini (yes/no)? ".format(hapus_produk_tertentu))
                        jawaban1 = jawaban1.lower()
                        while jawaban1.lower() not in ["yes", "no"]:
                            print("Mohon masukkan 'yes' atau 'no'")
                            jawaban1 = input("Apakah Kamu Yakin akan Menghapus Produk {} ini (yes/no)? ")
                        if jawaban1.lower() == "yes":
                            del list_iphone[i]
                            print("Produk dengan kode barang {} berhasil dihapus".format(hapus_produk_tertentu))
                            if len(list_iphone) == 0:
                                print("Maaf produk sudah terhapus semua kamu tdk dapat menghapus lagi")   
                            break
                        else:
                            print("Proses penghapusan dibatalkan.")
                            break
                    else:
                        i += 1
            
                if not produk_ditemukan: 
                   print("Kode Produk yang Anda Input tidak ditemukan.")
                
                
            elif hapus_produk == "2":
                break



def mengupdate_stock_produk():
    if not list_iphone:
        print("\n\n Maaf produk Iphone kosong, Anda tidak bisa lakukan update produk")
    else:
        while True:
            update_stock = input('''
---------------------------------------
**********UPDATE STOCK BARANG**********
---------------------------------------

1. Update Stock Produk disini : 
2. Kembali ke menu awal
                          
Silahkan input submenu yang akan dijalankan: ''') 
            if update_stock == "1":
                input_stock = input('''
Input Kode Produk Iphone yang akan diupdate dengan format,
[tipe HP brp/kapasitas RAM/warna] contohnya 11/64gb/hitam
jika iphone pro formatnya 14pro/256gb/hitam : ''')
                input_stock = input_stock.lower()
                produk_ditemukan = False
            
                for item in list_iphone:
                    if input_stock == item["kode barang"]:
                        print("| Kode Barang\t\t| Tipe Iphone\t| Stock\t| Harga\t\t| Kapasitas\t| Warna")
                        print("| {:<16}\t| {:<12}\t| {:<6}| {:<9}\t| {:<12}\t| {:<8}".format(item["kode barang"], item["tipe"], item["stock"], item["harga"], item["kapasitas"], item["warna"]))
                        produk_ditemukan = True
                        jawaban2 = input("Apakah ingin melanjutkan update stock produk (yes/no)?: ")
                        jawaban2 = jawaban2.lower()
                        if jawaban2 == "yes":
                            input_jawaban = int(input("Masukkan jumlah stock produknya menjadi berapa: "))
                            cek_jawaban = input("Apakah kode produk ({}) diupdate jadi {} (yes/no)? ".format(input_stock,input_jawaban))
                            cek_jawaban = cek_jawaban.lower()
                            if cek_jawaban == "yes":
                            
                                item["stock"] = input_jawaban
                                print("Update Stock Produk berhasil")
                            
                            
                        break  
             
                if not produk_ditemukan:
                    print("Produk tidak ditemukan")
                
            elif update_stock == "2":
                break


def mengurutkan_produk():
    if not list_iphone:
        print("\n\n Maaf produk Iphone habis, Anda tidak bisa mengurutkan produk") 
    else:      
        while True:
            urutan_produk = input('''
----------------------------------------
***********MENGURUTKAN PRODUK***********
----------------------------------------

1. Urutkan Produk sesuai Stock
2. Kembali ke menu awal
                          
Silahkan input submenu yang akan dijalankan: ''')
            if urutan_produk == "1":
                urutan_stock = input('''
                Pilihlah:

            1. Urutkan Produk dari Stock tertinggi ke terendah  
            2. Urutkan Produk dari Stock terendah ke tertinggi 
            3. kembali 
            
            Silahkan pilih angka yang ingin dijalankan: ''')
                if urutan_stock == "1":
                    n = len(list_iphone)
                    for i in range(n-1):
                        for j in range(i+1,n):
                            if list_iphone[i]["stock"]<list_iphone[j]["stock"]:
                                list_iphone[i]["stock"],list_iphone[j]["stock"] = list_iphone[j]["stock"],list_iphone[i]["stock"]

                    print("\n Daftar Produk yang sudah diurutkan berdasarkan Stock (dari tertinggi ke terendah):\n")
                    print("|Kode Barang\t\t|Tipe Iphone\t|Stock\t|Harga\t\t|Kapasitas\t|Warna")
                    for product in list_iphone:
                        print("|{:<16}\t| {:<12}\t| {:<6}| {:<9}\t| {:<12}\t| {:<8}".format(product["kode barang"], product["tipe"], product["stock"], product["harga"], product["kapasitas"], product["warna"]))
                

                    max_stock = list_iphone[0]["stock"]
                    for product in list_iphone:
                        if  product["stock"] > max_stock :
                            max_stock = product["stock"]
                        

                    print("\n\nStock Produk terbanyak adalah {}".format(max_stock))
                    print("\nYuk tingkatkan penjualan produk tersebut! SEMANGAT!!!")

                elif urutan_stock == "2":
                    n = len(list_iphone)
                    for i in range(n-1):
                        for j in range(i+1,n):
                            if list_iphone[i]["stock"]>list_iphone[j]["stock"]:
                                list_iphone[i]["stock"],list_iphone[j]["stock"] = list_iphone[j]["stock"],list_iphone[i]["stock"]

                    print("\n Daftar Produk yang sudah diurutkan berdasarkan Stock (dari tertinggi ke terendah):\n")
                    print("|Kode Barang\t\t|Tipe Iphone\t|Stock\t|Harga\t\t|Kapasitas\t|Warna")
                    for product in list_iphone:
                        print("|{:<16}\t| {:<12}\t| {:<6}| {:<9}\t| {:<12}\t| {:<8}".format(product["kode barang"], product["tipe"], product["stock"], product["harga"], product["kapasitas"], product["warna"]))
                
                    min_stock = list_iphone[0]["stock"]
                    for product in list_iphone:
                        if product["stock"] < min_stock:
                            min_stock = product["stock"]
                        
                    print("\n\nStock Produk paling sedikit adalah {}".format(min_stock))
                    print("\nYuk tambahkan lagi stock produk tersebut! ")
        
            elif urutan_produk == "2":
                break



while True:
    pilih_menu = input('''
======================================                   
Selamat Datang di Toko Iphone "Grace" 😊😊😊

======================================    
Daftar Menu :
-------------                   
    1. Menampilkan Daftar Produk
    2. Menambah Produk
    3. Menghapus Produk
    4. Mengupdate Stock Produk
    5. Urutkan produk 
    6. Exit
                       
        
Masukkan angka Menu yang ingin anda jalankan:''')

    if(pilih_menu == "1"):
        menampilkan_daftar_produk()

    elif(pilih_menu == "2") :
        menambah_produk()

    elif(pilih_menu == "3") :
        menghapus_produk()
    
    elif(pilih_menu == "4") :
        mengupdate_stock_produk()
    
    elif(pilih_menu == "5") :
        mengurutkan_produk()

    elif(pilih_menu == "6") :
        break