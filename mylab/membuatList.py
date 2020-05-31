# Membuat list dengan looping
numbers = [1, 2, 3, 4]
squares = []

for n in numbers:
    squares.append(n**2)

print(squares)

# Membuat list dengan List Comprehension
numbers = [1, 2, 3, 4]
squares = [n**2 for n in numbers]
print(squares)


# Menemukan bilangan yang ada di kedua list
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]

common_num = []

for a in list_a:
    for b in list_b:
        if a == b:
            common_num.append(a)

print(common_num)  # Output [2, 3, 4]

# Implementasi dengan list comprehension
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]

common_num = [a for a in list_a for b in list_b if a == b]

print(common_num)  # Output: [2, 3, 4]

# Kecilkan semua huruf
list_a = ["Hello", "World", "In", "Python"]

small_list_a = [_.lower() for _ in list_a]

print(small_list_a)  # Output: ['hello', 'world', 'in', 'python']

# Membuat list multidimensional
list_a = range(1, 10, 2)
x = [[a**2, a**3] for a in list_a]
print(x)
