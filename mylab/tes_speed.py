import time
from numba import jit


@jit(target='cpu', nopython=True)
def pungsi(N):
    j = 0
    for i in range(N):
        j = i + 100
        if(j % 2 == 0):
            j = 2
        while(j > N/10):
            j = j - 10
        continue
    return i


N = 300000
# start = time.time()
# hasil = pungsi(N)
#print('Total Processing Time Non JIT: %.2f seconds' % (time.time() - start))
start = time.time()

# dJIT=numba.jit(pungsi)
# hasil=dJIT(N)
hasil = pungsi(N)
print('Total Processing Time with JIT: %.2f seconds, hasil=%d' %
      ((time.time()-start), hasil))
# Total Processing Time with JIT: 4.18 seconds, hasil=299999
