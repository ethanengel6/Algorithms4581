import time
# Algorithm 1: Divide-and-Conquer
def DACcoins(coins, amount):
    if amount == 0: # The base case
        return 0
    else: # The recursive case
        minCoins = float("inf")
        for currentCoin in coins: # Check all coins
        # If we can give change
            if (amount - currentCoin) >= 0:
                # Calculate the optimal for currentCoin
                currentMin = DACcoins(coins, amount-currentCoin) + 1
#               Keep the best
                minCoins = min(minCoins, currentMin)
        return minCoins


def DPcoins(c, a):

  if a == 0: # The base case
    return 0
  M = [0]*(a+1)
  S = [0]*(a+1)

  for q in range(1,a+1):
    minimum = float('inf')
    coin = 0

    for i in range (1,len(c)):
      if q >= c[i]:
        minimum = min(minimum, 1+M[q-c[i]])
        coin = i
    M[q] = minimum
    S[q] = coin

  jingle = a
  while jingle>0:
    print(c[S[jingle]])
    jingle = jingle-c[S[jingle]]
  return M[a]




C = [1,5,10,12,25] # coin denominations (must include a penny)
A = int(input('Enter desired amount of change: '))
assert A>=0
print("DAC:")
t1 = time.time()
numCoins = DACcoins(C,A)
t2 = time.time()
print("optimal:",numCoins," in time: ",round((t2-t1)*1000,1),"ms")
print()
print("DP:")
t3 = time.time()
numCoins = DPcoins(C,A)
t4 = time.time()
print("optimal:",numCoins," in time: ",round((t4-t3)*1000,1),"ms")
