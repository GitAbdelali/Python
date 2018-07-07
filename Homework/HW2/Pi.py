def approxPIsquared(error):
  oldPi = 0
  i = 1
  while True:
    t = 8 / (2*i-1)**2
    newPi = oldPi + t
    if newPi - oldPi <= error:
      break

    oldPi = newPi
    i = i + 1

  return newPi


print(approxPIsquared(0.0001))
print(approxPIsquared(0.00000001))