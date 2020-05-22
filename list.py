# Modul copy hanya digunakan untuk menyalin List
import copy as cp

# Inisiasi List kosong
buah = []
print('Cetak List Kosong : ', buah)

# Inisiasi List dengan data
buah = ['Jeruk', 'Apel', 'Anggur']
print('Cetak List Dengan Data : ', buah)

# Mencetak list pada indeks tertentu
print('Cetak List Indeks 0 : ', buah[0])
print('Cetak List Indeks 1 : ', buah[1])

# Mendapatkan Indeks List
print('Anggur Terdapat Pada Indeks Ke-', buah.index('Anggur'))

# Menambah data pada list
buah = buah + ['Mangga']
buah += ['Jambu']
print('Menambah Mangga dan Jambu ke dalam list : ', buah)

# Cetak Panjang List
print('Panjang List : ', len(buah))

# Cetak Semua List
for nama_buah in buah:
    print('Buah Indeks Ke-', buah.index(str(nama_buah)), ' :', nama_buah)

# Update data pada list
buah[1] = 'Naga'
buah[4] = 'Melon'
print('Update List Buah Apel->Naga, Jambu->Melon : ', buah)

# Menambah List di akhir List
buah.append('Semangka')
print('Tambah Semangka di Akhir List : ', buah)

# Menambah List di Indeks Tertentu
buah.insert(3, 'Salak')
print('Tambah Salak di indeks 3 : ', buah)

# Menghapus List pada Indeks tertentu
del buah[2]
print('Menghapus List Pada Indeks Ke-2 : ', buah)

# Menghapus List dengan isi/nama tertentu
buah.remove('Salak')
print('Menghapus Data Salak : ', buah)

# Menyalin List dengan modul copy
my_fruits = cp.copy(buah)
print('List buah disalin ke list my_fruits : ', my_fruits)

# Mengurutkan List Ascending
my_fruits.sort()
print('Mengurutkan Secara Ascending', my_fruits)

# Mengurutkan List Descending
my_fruits.sort(reverse=True)
print('Mengurutkan Secara Descending', my_fruits)
