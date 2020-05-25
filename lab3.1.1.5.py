'''
Using one of the comparison operators in Python, 
write a simple two-line program that takes the parameter n as input, which is an integer, 
and prints False if n is less than 100, and True if n is greater than or equal to 100.
Don't create any if blocks (we're going to talk about them very soon). 
Test your code using the data we've provided for you.

Menggunakan operator komparasi buatlah program yang terdiri dari dua baris 
yang akan mencetak data dengan ketentuan sebagai berikut :
1. input berupa bilangan integer
2. jika input kurang dari 100 akan mencetak nilai False
3. dan jika input lebih besar atau sama dengan 100 akan mencetak nilai True 
'''
n = int(input('Masukan bilangan : '))

print(True if n >= 100 else False)
