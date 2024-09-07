print("Selamat Datang di Calculator")
print('''Pilihan:
1.Penjumlahan
2.Pengurangan
3.Perkalian
4.Pembagian
''')
pilihan = int(input("Masukan pilihan anda "))
if (pilihan == 1):
  print("Penjumlahan")
elif (pilihan == 2):
  print("Pengurangan")
elif (pilihan == 3):
  print("Perkalian")
elif (pilihan == 4):
  print("Pembagian")
elif (pilihan > 4):
  print("Masukan data yang sesuai")
else:
  print("Harap masukan angka")