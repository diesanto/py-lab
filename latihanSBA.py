class titik2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def ambiltitik(self):
        ambiltitik = (self.x, self.y)

        return ambiltitik

    def tambahkan(self, titik):
        x_baru, y_baru = titik

        x = self.x + x_baru
        y = self.y + y_baru

        return (x, y)


def run():
    titik = input('Masukan dua buah nilai, pisahkan dengan space :')
    x, y = titik.split(' ')

    return titik2d(float(x), float(y))
