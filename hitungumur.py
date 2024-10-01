import datetime as dt

def hidupmu():
    print("Menghitung berapa lama anda hidup")
    nama = str(input("Masukan nama anda: "))
    tanggal = int(input("Masukan tanggal lahir: "))
    bulan = int(input("Masukan bulan lahir: "))
    tahun = int(input("Masukan tahun lahir: "))
    tanggallahir = dt.date(tahun, bulan, tanggal)

    print("==========")
    print("Nama: " , nama)
    print("Tanggal Lahir anda: " , tanggallahir)
    hariIni = dt.date.today()
    lamahidup = hariIni - tanggallahir
    tahunlahir = lamahidup.days // 365
    bulanlahir = (lamahidup.days % 365) // 30
    hari_lahir = tanggallahir.strftime("%A")  # Mengambil nama hari lahir

    print(f"Lahir pada hari: {hari_lahir}")
    print(f"Lama hidup anda: {lamahidup.days} hari, sekitar {bulanlahir} bulan")
    print(f"Usia anda: {tahunlahir} tahun")

hidupmu()
