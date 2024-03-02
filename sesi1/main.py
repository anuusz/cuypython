import random

welcome_message = "WELCOME TO CUYPY GAMES!"
cuypy_position = random.randint(1, 4)

print("*****************************")
print(f"** {welcome_message} **")
print("*****************************")

nama_user = input("masukkan nama anda : ")
print(f'''Halo {nama_user}! Coba perhatikan goa dibawah ini
|__| |__| |__| |__|
''')

while True:
    pilihan_user = int(input("Menurut anda di goa nomor berapa CUYPY berada? [1 / 2 / 3 / 4] : "))

    konfirmasi = input("Apakah kamu yakin dengan pilihan tersebut? [y/n]: ")
    if konfirmasi.lower() == 'y':
        if pilihan_user == cuypy_position:
            print(f"Selamat {nama_user} kamu menang! posisi CUYPY ada di {cuypy_position} dan pilihanmu adalah {pilihan_user}.")
        else:
            print(f"Kamu Kalah, CUYPY tidak berada disitu!, tapi ada di goa nomor {cuypy_position} sedangkan kamu memilih {pilihan_user}.")
        break
    elif konfirmasi.lower() == 'n':
        print("program dihentikan.")
        exit()
    else:
        print("Input tidak valid. Mohon masukkan 'y' atau 'n'.")
