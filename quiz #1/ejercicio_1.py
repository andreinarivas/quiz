# =======================================================================
# Nombre del estudiante: Andreina Rivas
# Carnet: 20221110207
# =======================================================================

penta = [[45,78,65],[12,35,70],[51,3,105],[22,12,85]]
is_pen=True
pen_numbers=[]
pen=0
for lista in penta:
  for num in lista:
    for x in range(1,num+1):
    
        pen=((3*(x**2))-x)/2
        if pen<=num:
          if num == int(pen):
            is_pen=True
          else:
            is_pen=False
        else:
          break
    if is_pen:
      pen_numbers.append(num)

pen_numbers=set(pen_numbers)
print('Pentagon Numbers Found:')
for elements in pen_numbers:
  print("*{}".format(elements))
