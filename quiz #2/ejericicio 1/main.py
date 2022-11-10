# =======================================================================
# Nombre del estudiante: Andreina Rivas
# Carnet: 20221110207
# =======================================================================
from clases import Appliance, Washer, Microwave, Fridge, Blender


def create_appliance(dict): #extrae todos los datos de cada producto en general
  data=[]
  for key, value in dict.items():
    data.append(value)
  return data


def create_washer(dict, data_base): #crea el obejeto referente segun la lista retornada
  data=create_appliance(dict)
  data_base['Washers'].append(Washer(data[0], data[1], data[2], data[3], data[4]))

def create_microwave(dict, data_base):#crea el obejeto referente segun la lista retornada
  data=create_appliance(dict)
  data_base['Microwaves'].append(Microwave(data[0], data[1], data[2], data[3], data[4]))

def create_fridge(dict, data_base): #crea el obejeto referente segun la lista retornada
  data=create_appliance(dict)
  data_base['Fridges'].append(Fridge(data[0], data[1], data[2], data[3], data[4], data[5]))

def create_blender(dict, data_base): #crea el obejeto referente segun la lista retornada
  data=create_appliance(dict)
  data_base['Blenders'].append(Blender(data[0], data[1], data[2], data[3], data[4], data[5]))
        
def set_inventory(): #crea la base de datos a partir de objetos creados por las funciones anteriores
  edd = {
      "washer":
      [
          {"cod_p": "AEX-200918", "price": 551.99, "brand": "Whirlpool", "color": "Blanca", "capacity": 17},
          {"cod_p": "GHT-191214", "price": 409.00, "brand": "LG", "color": "Gris", "capacity": 15}
      ],
      "microwave":
      [
          {"cod_p": "FGE-220708", "price": 109.01, "brand": "Daewoo", "color": "Blanco", "digital": False},
          {"cod_p": "PEP-210123", "price": 201.50, "brand": "Frigilux", "color": "Negro", "digital": True}
      ],
      "fridge":
      [
          {"cod_p": "HYW-180909", "price": 280.98, "brand": "Electrolux", "color": "Plateado", "cooler": False, "comp": 5},
          {"cod_p": "IUO-201020", "price": 405.99, "brand": "Samsung", "color": "Azul pastel y rosado", "cooler": True, "comp": 8}
      ],
      "blender":
      [
          {"cod_p": "OWO-191111", "price": 42.05, "brand": "Oster", "color": "Plateado", "cup": "Cristal", "speeds": 3},
          {"cod_p": "XAT-221230", "price": 17.99, "brand": "Philips", "color": "Blanco", "cup": "Plastico", "speeds": 2}
      ]
  }
  data_base={'Washers': [], 'Microwaves': [], 'Fridges': [], 'Blenders': []} #mi base de datos para el ejercicio orientada a objetos
  for kind, product_list in edd.items(): #recorre la edd para crear las instancias y agregarlos a su espacio correspondiente
    if kind=='washer':
      for product in product_list:
        create_washer(product, data_base)
    if kind=='microwave':
      for product in product_list:
        create_microwave(product, data_base)
    if kind=='fridge':
      for product in product_list:
        create_fridge(product, data_base)
    if kind =='blender':
      for product in product_list:
        create_blender(product, data_base)
  return data_base

def print_database(data_base): # imprime mi base de datos ordenadamente
  for product_type, product_list in data_base.items():
    number=0
    print('\n ------ AVAILABLE {} ------'.format(product_type.capitalize()))
    for product in product_list:
      number+=1
      print('\n{} #{} \n'.format(product_type, number))
      product.show_info()

def validate_data_base(data_base,wanted): #valida que lo que quiero borrar existe en la base de datos
  exist=False
  for product_type, product_list in data_base.items():
      for product in product_list:
        if product.prod_id==wanted:
          exist=True 
  return exist

def search_data_base(data_base, wanted): #retorna la instancia que quiero agregar a mi lista de eliminados y la elimina de la base de datos
  for product_type, product_list in data_base.items():
      for product in product_list:
        if product.prod_id==wanted:
          data_base[product_type].remove(product)
          return product 

def validate_option(wanted, options, valid): #para imprimir todos mis menus y opciones
  option=input('\n {}\n Please enter an option: \n {} \n >>> '.format(wanted, options))
  while option not in valid:
    option=input('INVALID INPUT \n Please enter an option: \n {} \n >>> '.format(wanted, options))
  return int(option)

def print_fridges(data_base): #imprime solo las neveras y con sus atributos mas importantes 
  number=0
  for product_type, product_list in data_base.items():
    if product_type=='Fridges':
      print('\n ---------- FRIDGES AVAILABLE -----------')
      for product in product_list:
        number+=1
        print('\n FRIDGE #{}'.format(number))
        print('* Product ID: {}'.format(product.prod_id))
        print('* Brand: {}'.format(product.brand))
        print('* Price: {}'.format(product.price))
        if product.have_freezer:
          print('* Freezer: Yes')
        else:
          print('* Freezer: No')



def get_most_expensive(data_base): #encuentra el articulo mas costoso a partir de la base de datos mas actualizada
  max_price=0
  for product_type, product_list in data_base.items():
      for product in product_list:
        if product.price>max_price:
          max_price=product.price
          most_expensive=product
  return most_expensive
          



def main():
  eliminated=[]
  data_base=set_inventory()
  run=True
  while run:
    option=validate_option('WELCOME TO THE SYSTEM', '1. See inventory \n 2. Eliminate product \n 3. Quit', ['1', '2', '3'])


    if option==1: #todo lo referente al inventario (imprimir todo el inventario, solo las neveras disponibles, conseguir el producto mas caro)
      option_inventory=validate_option('INVENTORY MODULE', '1. Print inventory \n 2. Print fridges \n 3. Print most expensive item',  ['1', '2', '3'])
      if option_inventory==1:
        print_database(data_base)
      if option_inventory==2:
        print_fridges(data_base)
      if option_inventory==3:
        print('\n THE MOST EXPENSIVE ITEM \n')
        most_expensive=get_most_expensive(data_base)
        most_expensive.show_info()
      


    if option==2: #todo lo referente a eliminar (eliminar un producto segun su codigo, imprimir la lista de los productos elimindados)
      option_eliminate=validate_option('ELIMINATION MODULE', '1. Eliminate product\n 2. Print eliminated products', ['1', '2'])
      if option_eliminate==1:
        print('PRODUCT CODES:')
        for product_type, product_list in data_base.items():
          print('{}:'.format(product_type.capitalize()))
          for product in product_list:
            print('* {}'.format(product.prod_id))
        wanted=input('Please enter the code of the product you wish to remove: \n >>> ')
        while not validate_data_base(data_base, wanted):
          wanted=input('INVALID INPUT \n Please enter a valid product code: \n >>> ')
        to_delete=search_data_base(data_base, wanted)
        eliminated.append(to_delete)
        print('PRODUCT ELIMINATED')
      if option_eliminate==2:
        print('-------DELETED PRODUCTS--------')
        for x in range(len(eliminated)):
          print('\n DELETED PRODUCT #{}'.format(x+1))
          eliminated[x].show_info()


    if option==3:
      run=False


main()