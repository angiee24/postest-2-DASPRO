from prettytable import PrettyTable
import sys

#database untuk program dan metode pembayaran
program_donasi = ["Untuk panti jompo", "Untuk bencana alam"]
metode_pembayaran = ["Dana", "GoPay"]
donasi = []

#menampilkan tabel program dan metode
def menambah_tabel(data, judul):
    tabel = PrettyTable([judul])
    for item in data:
        tabel.add_row([item])
    print(tabel)

#tampilan awal
def menu_utama():
    while True:
        print("\n=== Layanan Donasi ===")
        print("[1]. Login Admin")
        print("[2]. Login User")
        print("[3]. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")
        if pilihan == '1':
            menu_admin()
        elif pilihan == '2':
            menu_user()
        elif pilihan == '3':
            print("Terima kasih telah menggunakan layanan donasi kami, Sampai jumpa!")
            sys.exit()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

#login admin
def menu_admin():
    while True:
        print("\n=== Menu Admin ===")
        print("[1]. Tambah Program atau Metode")
        print("[2]. Hapus Program atau Metode")
        print("[3]. Perbaiki Program atau Metode")
        print("[4]. Lihat Program dan Metode")
        print("[5]. Kembali")
        pilihan = input("Pilih menu Admin (1/2/3/4/5): ")
        if pilihan == '1':
            tambah_program_atau_metode()
        elif pilihan == '2':
            hapus_program_atau_metode()
        elif pilihan == '3':
            perbaiki_program_atau_metode()
        elif pilihan == '4':
            lihat_program_dan_metode()
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid.")

#menambah program atau metode pembayaran
def tambah_program_atau_metode():
    print("\nPilih yang ingin ditambahkan:")
    print("[1]. Program")
    print("[2]. Metode")
    pilihan = input("Pilih (1/2): ")
    if pilihan == '1':
        nama = input("Masukkan nama program baru: ")
        if nama not in program_donasi:
            program_donasi.append(nama)
            print(f"Program '{nama}' berhasil ditambahkan.")
        else:
            print("Program sudah ada.")
    elif pilihan == '2':
        nama = input("Masukkan nama metode baru: ")
        if nama not in metode_pembayaran:
            metode_pembayaran.append(nama)
            print(f"Metode '{nama}' berhasil ditambahkan.")
        else:
            print("Metode sudah ada.")
    else:
        print("Pilihan tidak valid.")

#menghapus program atau metode pembayaran
def hapus_program_atau_metode():
    print("\nPilih yang ingin dihapus:")
    print("[1]. Program")
    print("[2]. Metode")
    pilihan = input("Pilih (1/2): ")
    if pilihan == '1':
        hapus_item(program_donasi, "Program")
    elif pilihan == '2':
        hapus_item(metode_pembayaran, "Metode")
    else:
        print("Pilihan tidak valid.")

def hapus_item(daftar, data):
    menambah_tabel(daftar, data)
    item = input(f"Masukkan nama {data} yang ingin dihapus: ")
    if item in daftar:
        daftar.remove(item)  # Menggunakan item, bukan data
        print(f"{data} '{item}' berhasil dihapus.")  # Menampilkan item yang dihapus
    else:
        print(f"{data} tidak ditemukan.")

#memperbaiki program atau metode pembayaran
def perbaiki_program_atau_metode():
    print("\nPilih yang ingin diperbaiki:")
    print("[1]. Program")
    print("[2]. Metode")
    pilihan = input("Pilih (1/2): ")
    if pilihan == '1':
        perbaiki_daftar(program_donasi, "Program")
    elif pilihan == '2':
        perbaiki_daftar(metode_pembayaran, "Metode")
    else:
        print("Pilihan tidak valid.")

def perbaiki_daftar(daftar, data):
    menambah_tabel(daftar, data)
    nama_lama = input(f"Masukkan nama {data} yang ingin diperbaiki: ")
    if nama_lama in daftar:
        nama_baru = input(f"Masukkan nama baru untuk {data} '{nama_lama}': ")
        if nama_baru not in daftar:
            posisi = daftar.index(nama_lama)
            daftar[posisi] = nama_baru
            print(f"{data} '{nama_lama}' berhasil diperbaiki menjadi '{nama_baru}'.")
        else:
            print(f"{data} '{nama_baru}' sudah ada.")
    else:
        print(f"{data} tidak ditemukan.")

#menampilkan program dan metode pembayaran
def lihat_program_dan_metode():
    menambah_tabel(program_donasi, "Program")
    menambah_tabel(metode_pembayaran, "Metode")

#login user
def menu_user():
    print("\n=== Selamat Datang User ===")
    donatur = input("Masukkan Nama/Instansi Anda: ")
    donasi_user(donatur)

def donasi_user(donatur):
    menambah_tabel(metode_pembayaran, "Metode Pembayaran")
    pilih_metode = input("Pilih metode pembayaran: ")

    if pilih_metode in metode_pembayaran:
        menambah_tabel(program_donasi, "Program Donasi")
        program = input("Pilih program donasi: ")

        if program in program_donasi:
            
            nominal = input("Masukkan nominal donasi: ")
            donasi.append({"Donatur": donatur, "Program": program, "Metode": pilih_metode, "Nominal": nominal})
            print(f"Terima kasih {donatur}, Anda telah berdonasi sebesar Rp {nominal} untuk program '{program}' melalui metode '{pilih_metode}'.")
            sys.exit()  
        else:
            print("Program tidak ditemukan.")
    else:
        print("Metode pembayaran tidak valid.")

menu_utama()
