# -*- coding: utf-8 -*-
"""My Project 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14UF1wr9PflFUq5B51IIVTjuH4ag4x0WT
"""

#Graded

def isPointInCircle(x,y,r,center=(0,0)):
  # MULAI KODEMU DI SINI
  pass
  
  L = (x-center[0])**2 + (y-center[1])**2

  if L < r**2:
    return True
  elif L == r**2:
    return True
  elif L > r**2:
    return False

print(isPointInCircle(1,1,1,center=(0,0)),isPointInCircle(1,0,1,center=(0,0)),
      isPointInCircle(1,1,1,center=(1,0)),isPointInCircle(0,0,1,center=(1,1)))

#Graded
import random


def generateRandomSquarePoints(n,length,center=(0,0)):
  # MULAI KODEMU DI SINI
  minx = center[0]-length/2
  miny = center[1]-length/2
  
  # Gunakan list comprehension dengan variable minx, miny, length, dan n
  points = [[random.uniform(minx, (minx+length)), random.uniform(miny, (miny+length))] for x in range(n)]

  return points

#CEK OUTPUT KODE ANDA
random.seed(0)

# generate 100 point di dalam persegi dengan panjang sisi 1 dan berpusat di (0,0)
points = generateRandomSquarePoints(100,1)
print(points[10:15])

#CEK OUTPUT KODE ANDA VISUALISASI
# Mari kita Visualisasikan 
# Jika sama dengan gambar di bawah ini maka keluaran sesuai harapan
import matplotlib.pyplot as plt
x,y = zip(*points)

# persegi dengan panjang sisi 1 dan berpusat di (0,0)
r1 = plt.Rectangle((-0.5,-0.5),1,1,color='r', fill=False)
c1 = plt.Circle((0,0), 0.5, color='b', fill=False)
fig, ax = plt.subplots(figsize=(9,9)) 
ax.add_artist(r1)
ax.add_artist(c1)
plt.xlim(-0.6,0.6)
plt.ylim(-0.6,0.6)
plt.scatter(x,y,s=100,marker='x')
plt.show()

#Graded

def MCCircleArea(r,n=100,center=(0,0)):
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



#CEK OUTPUT KODE ANDA

random.seed(0)
print(MCCircleArea(1,100),MCCircleArea(1,10,center=(10,10)))

#Graded

def LLNPiMC(nsim,nsample):
  # MULAI KODEMU DI SINI
  pass
  x = 0
  for i in range(nsim): 
    x += MCCircleArea(1,nsample)

  return x/nsim

#CEK OUTPUT KODE ANDA

import math

random.seed(0)
estpi = LLNPiMC(10000,500)

print('est_pi:',estpi)
print('act_pi:',math.pi)

# Graded
def relativeError(act,est):
  
  # MULAI KODEMU DI SINI
  pass
  return abs((est-act)/act)* 100

#CEK OUTPUT KODE ANDA
print('error relatif:',relativeError(math.pi,estpi),'%')