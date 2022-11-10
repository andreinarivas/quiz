# =======================================================================
# Nombre del estudiante: Andreina Rivas
# Carnet: 20221110207
# =======================================================================

class Appliance:
  def __init__(self,prod_id, price, brand, color):
    self.prod_id=prod_id
    self.price=price
    self.brand=brand
    self.color=color

  def show_info(self):
    for info, data in self.__dict__.items():
      print('{}: {}'.format(info.capitalize(), data))
    print('\n')

class Washer(Appliance):
  def __init__(self, prod_id, price, brand, color, capacity):
    Appliance.__init__(self, prod_id, price, brand, color)
    self.capacity=capacity

class Microwave(Appliance):
  def __init__(self, prod_id, price, brand, color, control):
    Appliance.__init__(self, prod_id, price, brand, color)
    self.control=control
  
class Fridge(Appliance):
  def __init__(self, prod_id, price, brand, color, have_freezer, comp):
    Appliance.__init__(self, prod_id, price, brand, color)
    self.have_freezer=have_freezer
    self.compartments=comp

class Blender(Appliance):
  def __init__(self, prod_id, price, brand, color, material, speeds):
    Appliance.__init__(self, prod_id, price, brand, color)
    self.material=material
    self.speeds=speeds

