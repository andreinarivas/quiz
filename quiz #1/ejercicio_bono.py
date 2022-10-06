# =======================================================================
# Nombre del estudiante: Andreina Rivas
# Carnet: 20221110207
# =======================================================================

num=input('Please enter a round number: \n >>> ')
digits=[]
while not num.isnumeric():
  num=input('Invalid input. \n Please enter a round number: \n >>> ')
digits=[int(x) for x in num]
is_repunit=True
for x in digits:
  if x!=digits[0]:
    is_repunit=False
if is_repunit==True:
  print('The number {} is Repunit'.format(num))
else:
  print('The number {} is not Repunit'.format(num))