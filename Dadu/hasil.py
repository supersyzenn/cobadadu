# hasil di isi oleh output dari cobadadu.py dan di bawah ini contoh hasil dari lempar dadu
hasil = ["5", "4", "3", "6", "3", "3", "4", "6", "4", "5"]


rekapHasil = {}

for data in hasil:
    if data in rekapHasil:
        rekapHasil[data] += 1
    else:
        rekapHasil[data] = 1

print(rekapHasil)
