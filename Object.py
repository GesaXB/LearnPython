# Kelas
class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk  # Atribut
        self.warna = warna  # Atribut

    def __str__(self): #Method
        return f'Mobil ini adalah {self.merk} berwarna {self.warna}.'

# Membuat objek dari kelas Mobil
mobil_saya = Mobil('Honda', 'Putih')
mobil_kamu = Mobil('Toyota', 'Hitam')

# Mengakses atribut dan mode objek
print(mobil_saya) 
print(mobil_kamu)  
