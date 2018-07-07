def statement(balanceSheet):
  dAmount = 0
  wAmount = 0
  for transactionOf in balanceSheet:
    if transactionOf > 0: 
      dAmount += transactionOf
    else: 
      wAmount += transactionOf 
  return [dAmount, wAmount]

print(statement([30.95, -15.67, 45.56, -55.00, 43.78]))