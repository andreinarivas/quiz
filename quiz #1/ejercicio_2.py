# =======================================================================
# Nombre del estudiante: Andreina Rivas
# Carnet: 20221110207
# =======================================================================
anime = {
    "Demon Slayer": {
        "Temporada 1": [
        {
            "cap": 1,
            "name": "Crueldad",
            "duration": "23:39"
        },
        {
            "cap": 4,
            "name": "Selección final",
            "duration": "23:40"
        },
        {
            "cap": 19,
            "name": "Dios del fuego",
            "duration": "23:40"
        },
        {
            "cap": 26,
            "name": "Una nueva misión",
            "duration": "24:10"
        }
    ],
        "Temporada 2": [
        {
            "cap": 26,
            "name": "Un sueño profundo",
            "duration": "22:55"
        },
        {
            "cap": 43,
            "name": "¡No me rendiré!",
            "duration": "23:40"
        }
    ]
 
        },
    "Spy x Family": {
       
        "Temporada 1":[
        {
            "cap": 4,
            "name": "Objetivo: pasar la entrevista",
            "duration": "24:10"
        },
        {
            "cap": 7,
            "name": "El segundo hijo del objetivo",
            "duration": "24:10"
        }
    ]
    },
    "Attack on Titan": {
        "Temporada 3": [
            {
                "cap": 46,
                "name": "La reina de la muralla",
                "duration": "23:55"
            },
            {
                "cap": 54,
                "name": "Héroe",
                "duration": "23:55"
            }
    ],
        "Temporada 4":[
            {
                "cap": 60,
                "name": "Al otro lado del mar",
                "duration": "23:55"
            },
            {
                "cap": 72,
                "name": "Los hijos del bosque",
                "duration": "23:55"
            }
        ]
        }
}

run='yes'
history={}
watch_number=0
while run=='yes':
  print('\nBienvenido a Anima-te-ve ㊗️.\n Que quieres hacer hoy?')
  option=input('\nIntroduce una opcion valida: \n1. Escoger show\n2. Ver historial \n3.Salir \n>>> ')
  while not option.isnumeric() and not option in ["1","2"]:
    option=input('ERROR \nIntroduce una opcion valida: \n1. Escoger show\n2. Ver historial \n3.Salir \n>>> ')
  option=int(option)
  if option==1:
    watch_number+=1
    new_watch={}
    print("***** ESCOGER SHOW *****\n SHOWS DISPONIBLES:\n")
    for shows in anime.keys():
      print('*. {}'.format(shows))
    select_show=input('\n Por favor introduce el nombre del show que deseas ver: \nNOTA: Escribelo tal como se muestra en pantalla\n  >>> ')
    print("***** TEMPORADAS DISPONIBLES *****\n")
    for seasons in anime[select_show].keys():
        print('*. {}'.format(seasons))
    select_season=input('Por favor selecciona la temporada que seaseas ver: \n Introducir el número de temporada\n >>> ')
    season='Temporada {}'.format(select_season)
    for x in anime[select_show][season]:
        for info, data in x.items():
          print('{}: {}'.format(info.capitalize(),data))
        print('\n')
    cap_selected=input('Por favor introduzca el numero de capitulo que desea ver: \n >>> ')
    for x in anime[select_show][season]:
        for info, data in x.items():
          if info=='cap':
            if data==cap_selected:
              cap_key=x
    new_watch['show']=select_show
    new_watch['temporada']= season
    new_watch['capitulo']=x
    history[watch_number]=new_watch
    print('CAPITULO SELECCIONADO \n')
    for key, value in new_watch.items():
        if key=='capitulo':
          for info,data in value.items():
            print('{}: {}'.format(info.title(),data))
        else:
          print('{}: {}'.format(key.title(),value))
  if option==2:
    print('***** HISTORIAL DE REPRODUCCION *****')
    for i in history.keys():
      print('\nWATCH #{}'.format(i))
      for key, value in history[i].items():
        if key=='capitulo':
          for info,data in value.items():
            print('{}: {}'.format(info.title(),data))
        else:
          print('{}: {}'.format(key.title(),value))
  if option==3:
    run='no'

print('Gracias por usar nuestro servicio!')
    

      
      

    
    