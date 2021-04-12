# nama file p2.py
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded

# untuk revisi dan resubmisi sebelum deadline
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0
priority = 0

# netacad email cth: 'abcd@gmail.com'
email = 'herdiesel.santoso@gmail.com'

# copy-paste semua #Graded cells YANG SUDAH ANDA KERJAKAN di bawah ini


# Graded
def isPointInCircle(x, y, r, center=(0, 0)):
    # MULAI KODEMU DI SINI
    pass

    L = (x-center[0])**2 + (y-center[1])**2

    if L < r**2:
        return True
    elif L == r**2:
        return True
    elif L > r**2:
        return False


# Graded
import random
def generateRandomSquarePoints(n, length, center=(0, 0)):
    # MULAI KODEMU DI SINI
    minx = center[0]-length/2
    miny = center[1]-length/2

    # Gunakan list comprehension dengan variable minx, miny, length, dan n
    points = [[random.uniform(
        minx, (minx+length)), random.uniform(miny, (miny+length))] for x in range(n)]

    return points


# Graded
def MCCircleArea(r, n=100, center=(0, 0)):
    # MULAI KODEMU DI SINI
    pass
    length = 2 * r
    points = generateRandomSquarePoints(n, length, center)

    ntitik_dalam_lingkaran = 0
    for point in points:
        if isPointInCircle(point[0], point[1], r, center) == True:
            ntitik_dalam_lingkaran += 1

    luas_lingkaran = (ntitik_dalam_lingkaran/n) * (length ** 2)

    return luas_lingkaran


# Graded
def LLNPiMC(nsim, nsample):
    # MULAI KODEMU DI SINI
    pass
    x = 0
    for i in range(nsim):
        x += MCCircleArea(1, nsample)

    return x/nsim


# Graded
def relativeError(act, est):

    # MULAI KODEMU DI SINI
    pass
    return abs((est-act)/act) * 100
