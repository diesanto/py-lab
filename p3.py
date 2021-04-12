# nama file p3.py
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded

# untuk revisi dan resubmisi sebelum deadline
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0
priority = 1

# netacad email cth: 'abcd@gmail.com'
email = 'herdiesel.santoso@gmail.com'

# copy-paste semua #Graded cells YANG SUDAH ANDA KERJAKAN di bawah ini

# Graded
def caesar_encript(txt, shift):
    pass
    # Mulai Kode anda di sini
    caesar_encript = []
    for i in range(len(txt)):
        num = txt[i]
        if (num.isalpha()) == True:
            up = num.upper()
            num = chr((((ord(up) + shift) + 65) % 26) + 65)

            if (txt[i].islower()) == True:
                num = num.lower()

        caesar_encript.append(num)

    return ''.join(caesar_encript)

# Graded
# Fungsi mengacak urutan
def shuffle_order(txt, order):
    return ''.join([txt[i] for i in order])

# Fungsi untuk mengurutkan kembali sesuai order
def deshuffle_order(sftxt, order):
    # Mulai Kode anda di sini
    res = [None] * len(sftxt)
    for i, j in enumerate(order):
        res[j] = sftxt[i]

    return ''.join(res)

# Graded
# convert txt ke dalam bentuk list teks yang lebih pendek
# dan terenkrispi dengan urutan acak setiap batchnya
import math
def send_batch(txt, batch_order, shift=3):
    pass
    # Mulai Kode anda di sini
    line = caesar_encript(txt, shift)
    x = []
    n = len(batch_order)
    for i in range(0, len(line), n):
        y = line[i:i+n]

        if len(y) < n:
            for j in range(n - len(y)):
                y += '_'

        x += [shuffle_order(y, batch_order)]

    return x
