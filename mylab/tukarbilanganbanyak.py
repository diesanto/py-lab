# Masukan bilangan pertama
bil1 = int(input('Masukan bilangan ke - 1 : '))
# Masukan bilangan kedua
bil2 = int(input('Masukan bilangan ke - 2 : '))
# Masukan bilangan ketiga
bil3 = int(input('Masukan bilangan ke - 3 : '))

print('Bilangan ke - 1 sebelum di tukar : ', bil1)
print('Bilangan ke - 2 sebelum di tukar : ', bil2)
print('Bilangan ke - 3 sebelum di tukar : ', bil3)

# Tukar bilangan
bil1, bil2, bil3 = bil2, bil3, bil1

print('\n====== Setelah Pertukaran ========\n')
print('Bilangan ke - 1 setelah di tukar : ', bil1)
print('Bilangan ke - 2 setelah di tukar : ', bil2)
print('Bilangan ke - 3 setelah di tukar : ', bil3)
