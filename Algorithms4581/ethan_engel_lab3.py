import math,random,time
import pandas as pd
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

def isPrime(p):
    for q in range(2, int(math.sqrt(p)+1)):
        if p%q==0:
            return False
    return True

def nBitPrime(n):
    q=1
    while q>0:
        randPrime=int(random.random()*2**n)
        if randPrime>=2 and isPrime(randPrime)==True:
            return randPrime


def factor(pq):
    for zz in range(2, int(math.sqrt(pq)+1)):
        if pq%zz==0:
            return zz, int(pq/zz)

def exp_fit(x,a,b,c):
    return a*np.exp(b*x)+c


data=[]
for cc in range(15,30):
    pq=nBitPrime(cc)*nBitPrime(cc)
    t1=time.time()
    B = factor(pq)
    t2 = time.time()
    FactorTime = round((t2-t1)*1000,1)
    print(cc,FactorTime)
    data.append([cc,FactorTime])
df=pd.DataFrame(data=data,columns=['bits','time'])
runtime=np.array(df['time'])
bits=np.linspace(15,len(runtime)+15,len(runtime))
fit = curve_fit(exp_fit,bits,runtime,p0=[1,1e-6,1],maxfev=10000)
fit_eq=fit[0][0]*np.exp(fit[0][1]*bits)+fit[0][2]
print(fit[0][0],round(fit[0][1],3),round(fit[0][2],3))

fig=plt.figure()
ax=fig.subplots()
ax.scatter(bits,runtime,color='b',s=5)
ax.plot(bits,fit_eq,color='r',alpha=.7)
ax.set_ylabel("Run time")
ax.set_xlabel("# of bits")
plt.show()

# One of the run-throughs of the code yielded an exponential model of f(x)=(9.635876287773174e-11)*exp(1.147x)+1681.139, where x is the # of bits of the encryption #
#and f(x) is the run time in milliseconds.  This predicts a runtime of 1.188*10^500 milliseconds for a 1024 bit encryption value. This is approximately
#3.767*10^489 years, an unattainable time horizon.
