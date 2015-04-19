for i in range(1,10):
  for j in range(i,10):
    formula=str.format('{0}*{1}={2:<2}',i,j,i*j)
    print(formula,end=' ')
  print()
  for k in range(1,i+1):
    print(end='       ')
  
