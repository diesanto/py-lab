# Script menghitung nilai rata-rata siswa dengan list dan looping
# Input nilai siswa akan berhenti jika diinputkan nilai 0
# Output nilai rata-rata siswa

data_nilai = []
i = 1

while True:
    print('Masukan nilai siswa ke-', str(i), ' :', end=' ')
    x = int(input())
    if x == 0:
        break
    else:
        data_nilai += [x]
    i = i + 1

sum = 0
for nilai in data_nilai:
    sum += nilai

rata2nilai = sum/(len(data_nilai))

print('Nilai rata-rata siswa adalah ', rata2nilai)
