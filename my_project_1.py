# nama file p1.py
# Isikan nama anda dan copy semua cell code yang dengan komentar #Graded
nama = 'Herdiesel Santoso'
# netacad email cth: 'abcd@gmail.com'
email = 'herdiesel.santoso@gmail.com'

# copy-paste semua #Graded cells di bawah ini

# 1. Graded
# PASTE KODE ANDA DISINI


def letter_catalog(items, letter='A'):
    pass
    # MULAI KODEMU DI SINI
    letter_catalog = []
    for item in items:
        if item[0] == letter:
            letter_catalog.append(item)

    # print(letter_catalog)
    return letter_catalog


# Cek output kode anda
letter_catalog(['Apple', 'Avocado', 'Banana', 'Blackberries',
                'Blueberries', 'Cherries'], letter='C')

# 2. Graded


def counter_item(items):
    pass
    # MULAI KODEMU DI SINI
    counter_item = {}
    for item in items:
        item_count = items.count(item)
        counter_item[item] = item_count

    # print(counter_item)
    return counter_item


counter_item(['Apple', 'Apple', 'Apple', 'Blueberries',
              'Blueberries', 'Blueberries'])
# 3. Graded
# dua variable berikut jangan diubah
fruits = ['Apple', 'Avocado', 'Banana', 'Blackberries', 'Blueberries',
          'Cherries', 'Date Fruit', 'Grapes', 'Guava', 'Jackfruit', 'Kiwifruit']
prices = [6, 5, 3, 10, 12, 7, 14, 15, 8, 7, 9]

# list buah
chart = ['Blueberries', 'Blueberries', 'Grapes', 'Apple', 'Apple',
         'Apple', 'Blueberries', 'Guava', 'Jackfruit', 'Blueberries', 'Jackfruit']

# MULAI KODEMU DI SINI
fruit_price = {}
chart.sort()

for i in range(len(fruits)-1):
    # fruit_price[fruits[i]] = prices[i] atau
    fruit_price.update({fruits[i]: prices[i]})


def total_price(dcounter, fprice):
    pass
    # MULAI KODEMU DI SINI
    total_price = 0
    for f, i in dcounter.items():
        total_price += i * fprice[f]

    return total_price


total_price(counter_item(chart), fruit_price)

# 4. Graded


def discounted_price(total, discount, minprice=100):
    pass
    # MULAI KODEMU DI SINI
    if total > minprice:
        discounted_price = total - (total * (discount/100))
        return discounted_price
    else:
        return total


discounted_price(total_price(counter_item(
    chart), fruit_price), 10, minprice=100)

# Graded


def print_summary(items, fprice):
    pass
    # MULAI KODEMU DI SINI
    dcounter = counter_item(items)
    for f, i in dcounter.items():
        print(i, f, ':', i * fprice[f], sep=' ')

    print('\ntotal : ', total_price(counter_item(items), fprice))
    print('\ndiscount price :', discounted_price(
        total_price(counter_item(items), fprice), 10, minprice=100))


print_summary(chart, fruit_price)
