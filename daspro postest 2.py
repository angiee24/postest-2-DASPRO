donations = []
programs = {}
methods = {}

# Menambahkan data
def inisialisasi_data_awal():
    programs["Untuk yatim piatu"] = {}
    programs["Untuk bencana alam"] = {}
    methods["Dana"] = True
    methods["GoPay"] = True

# Fungsi untuk menampilkan menu utama
def tampilkan_menu_utama():
    print("\n=== Layanan Donasi ===")
    print("1. Login sebagai Admin")
    print("2. Login sebagai User")
    print("3. Keluar")

# Fungsi untuk menampilkan menu admin
def tampilkan_menu_admin():
    print("\n=== Menu Admin ===")
    print("1. Tambah Program atau Metode")
    print("2. Hapus Program atau Metode")
    print("3. Lihat Program dan Metode")
    print("4. Perbarui Program atau Metode")
    print("5. Kembali")

# Menambah program atau metode
def tambah_program_dan_metode():
    print("\n=== Pilih yang ingin ditambahkan ===")
    print("1. Tambah Program")
    print("2. Tambah Metode")
    pilihan = input("Pilih (1/2): ")

    if pilihan == '1':
        tambah_program()
    elif pilihan == '2':
        tambah_metode()
    else:
        print("Pilihan tidak valid.")

# Fungsi untuk menambah program
def tambah_program():
    nama_program = input("Masukkan nama program baru: ")
    programs[nama_program] = {}
    print(f"Program '{nama_program}' berhasil ditambahkan.")

# Fungsi untuk menambah metode
def tambah_metode():
    nama_metode = input("Masukkan nama metode baru: ")
    methods[nama_metode] = True
    print(f"Metode '{nama_metode}' berhasil ditambahkan.")

# Fungsi untuk menghapus program
def hapus_program():
    if not programs:
        print("Tidak ada program yang dapat dihapus.")
        return

    print("\n=== Pilih Program yang ingin dihapus ===")
    for i, program in enumerate(programs.keys(), start=1):
        print(f"{i}. {program}")
    
    program_pilihan = int(input("Pilih program (nomor): ")) - 1
    program = list(programs.keys())[program_pilihan]

    if program in programs:
        del programs[program]
        print(f"Program '{program}' berhasil dihapus.")
    else:
        print("Program tidak ditemukan.")

# Fungsi untuk menghapus metode
def hapus_metode():
    if not methods:
        print("Tidak ada metode yang dapat dihapus.")
        return

    print("\n=== Pilih Metode yang ingin dihapus ===")
    for i, metode in enumerate(methods.keys(), start=1):
        print(f"{i}. {metode}")
    
    metode_pilihan = int(input("Pilih metode (nomor): ")) - 1
    metode = list(methods.keys())[metode_pilihan]

    if metode in methods:
        del methods[metode]
        print(f"Metode '{metode}' berhasil dihapus.")
    else:
        print("Metode tidak ditemukan.")

# Fungsi untuk memperbarui program
def perbarui_program():
    if not programs:
        print("Tidak ada program yang dapat diperbarui.")
        return

    print("\n=== Pilih Program yang ingin diperbarui ===")
    for i, program in enumerate(programs.keys(), start=1):
        print(f"{i}. {program}")

    program_pilihan = int(input("Pilih program (nomor): ")) - 1
    program = list(programs.keys())[program_pilihan]
    nama_baru = input("Masukkan nama baru untuk program ini: ")
    
    programs[nama_baru] = programs.pop(program)
    print(f"Program '{program}' berhasil diperbarui menjadi '{nama_baru}'.")

# Fungsi untuk memperbarui metode
def perbarui_metode():
    if not methods:
        print("Tidak ada metode yang dapat diperbarui.")
        return

    print("\n=== Pilih Metode yang ingin diperbarui ===")
    for i, metode in enumerate(methods.keys(), start=1):
        print(f"{i}. {metode}")

    metode_pilihan = int(input("Pilih metode (nomor): ")) - 1
    metode = list(methods.keys())[metode_pilihan]
    nama_baru = input("Masukkan nama baru untuk metode ini: ")

    methods[nama_baru] = methods.pop(metode)
    print(f"Metode '{metode}' berhasil diperbarui menjadi '{nama_baru}'.")

# Fungsi untuk memperbarui program dan metode
def perbarui_program_dan_metode():
    print("\n=== Pilih yang ingin diperbarui ===")
    print("1. Perbarui Program")
    print("2. Perbarui Metode")
    pilihan = input("Pilih (1/2): ")

    if pilihan == '1':
        perbarui_program()
    elif pilihan == '2':
        perbarui_metode()
    else:
        print("Pilihan tidak valid.")

# Fungsi untuk melihat program dan metode
def lihat_program_dan_metode():
    print("\n=== Daftar Program ===")
    if not programs:
        print("Belum ada program yang ditambahkan.")
    else:
        for program in programs.keys():
            print(f"Program: {program}")

    print("\n=== Daftar Metode ===")
    if not methods:
        print("Belum ada metode yang ditambahkan.")
    else:
        for metode in methods.keys():
            print(f"Metode: {metode}")

# Fungsi untuk login admin
def login_admin():
    while True:
        tampilkan_menu_admin()
        pilihan = input("Pilih menu Admin (1/2/3/4/5): ")

        if pilihan == '1':
            tambah_program_dan_metode()
        elif pilihan == '2':
            hapus_program()
            hapus_metode()
        elif pilihan == '3':
            lihat_program_dan_metode()
        elif pilihan == '4':
            perbarui_program_dan_metode()
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid.")

# Fungsi untuk melakukan donasi oleh user
def donasi_user(donatur):
    while True:  # Loop untuk memastikan user memilih metode yang valid
        print("\n=== Pilih Metode Pembayaran ===")
        if not methods:
            print("Tidak ada metode yang tersedia. Silakan hubungi Admin.")
            return

        for i, metode in enumerate(methods.keys(), start=1):
            print(f"{i}. {metode}")

        metode_pilihan = int(input("Pilih metode (nomor): ")) - 1
        if 0 <= metode_pilihan < len(methods):
            metode = list(methods.keys())[metode_pilihan]
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            continue  # Kembali ke awal loop untuk memilih metode lagi

        while True:  # Loop ini hanya untuk pemilihan program
            print("\n=== Pilih Program Donasi ===")
            if not programs:
                print("Tidak ada program yang tersedia. Silakan hubungi Admin.")
                return

            for i, program in enumerate(programs.keys(), start=1):
                print(f"{i}. {program}")

            program_pilihan = int(input("Pilih program (nomor): ")) - 1
            if 0 <= program_pilihan < len(programs):
                program = list(programs.keys())[program_pilihan]
                break  # Jika program valid, keluar dari loop program
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

        while True:  # Loop ini hanya untuk pemilihan nominal
            print("\n=== Pilih Nominal Donasi ===")
            print("1. 25.000")
            print("2. 50.000")
            print("3. 100.000")
            print("4. Masukkan nominal sendiri")
            pilihan_nominal = input("Pilih nominal (1/2/3/4): ")

            if pilihan_nominal == '1':
                nominal = 25000
                break  # Jika pilihan nominal valid, keluar dari loop nominal
            elif pilihan_nominal == '2':
                nominal = 50000
                break
            elif pilihan_nominal == '3':
                nominal = 100000
                break
            elif pilihan_nominal == '4':
                nominal = float(input("Masukkan nominal custom: "))
                if nominal > 0:  # Pastikan nominal lebih besar dari 0
                    break
                else:
                    print("Nominal tidak valid. Masukkan angka yang benar.")
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

        # Simpan donasi
        donations.append({'donatur': donatur, 'metode': metode, 'program': program, 'nominal': nominal})
        print(f"Terima kasih {donatur} atas donasi sebesar Rp {nominal} untuk program '{program}' menggunakan metode '{metode}'.")
        print("Anda telah selesai melakukan donasi.")
        break  

# Fungsi untuk login user
def login_user():
    print("=" * 10 + " Selamat Datang Pembeli! ")
    donatur = input("Sebutkan Nama/Instansi Anda: ")
    print(f"Selamat datang, {donatur}!")

    # Langsung menuju proses donasi
    donasi_user(donatur)

# Program Utama
inisialisasi_data_awal()
while True:
    tampilkan_menu_utama()
    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == '1':
        login_admin()
    elif pilihan == '2':
        login_user()
    elif pilihan == '3':
        print("Terima kasih telah menggunakan layanan donasi. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid.")
