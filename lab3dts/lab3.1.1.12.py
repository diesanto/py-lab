'''
Pada suatu masa terdapat sebuah daratan - daratan dengan susu dan madu, yang dihuni oleh masyarakat yang bahagia dan sejahtera. Masyarakat tersebut membayar pajak, sehingga kebahagiaan mereka memiliki batas. Pajak yang paling penting adalah Personal Income Tax atau disebut PIT yang mana harus dibayarkan tiap tahun, dan dievaluasi dengan peraturan sebagai berikut :

Jika penghasilan tidak lebih besar daripada 85,528 thaler, maka pajak adalah sebesar 18% dari pemasukan dikurangi 556 thaler dan 2 sen (disebut juga tax relief)
Jika penghasilan lebih dari nilai tersebut, maka pajak adalah sebesar 14,839 thaler and 2 cents, ditambah 32% dari selisih penghasilan dengan 85,528 thalers.
Tugas anda adalah membuat tax calculator.

Harus menerima satu masukan : penghasilan
Berikutnya, print pajak yang telah dihitung, nilai dibulatkan penuh ke thaler (tanpa sen). Fungsi round() akan membantu anda untuk membulatkan nilai.
Catatan : Negara yang bahagia ini tidak pernah mengembalikan uang tersebut ke warganya. Jika perhitungan pajak kurang dari nol, itu berarti warga tidak dikenakan pajak sama sekali (pajak = 0).

Perhatikan syntax dibawah ini, hanya membaca satu input dan output sebagai hasilnya. Lengkapi syntax tersebut dengan sebuah perhitungan yang cerdas.
'''

income = float(input("Enter the annual income: "))
tax = 0

if income < 85528:
    tax = 0.18 * income - 556.2
else:
    tax = 14839 + 0.2 + 0.32 * (income - 85528)

tax = round(tax, 0)

if tax<0:
    tax = 0

print("The tax is:", tax, "thalers")