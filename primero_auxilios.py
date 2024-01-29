#Patricio Carrasco
print("aplicacion de salud")

estimulo = input(" el paciente responde a estimulos? 1(SI) 2(NO): ")


if respuesta_1 == '1':
    print('>>>Debes valorar la necesidad de llevarlo al hospital más cercano')
    print('-'*80)
    print('Fin de las recomendaciones\n')
else: 
    print('>>>Debes abrir la vía Aérea')
    print('-'*80)
    respuesta_2 = input('¿La persona respira? \n 1: SI \n 2: NO \nRespuesta: ')
    print('-'*80)
    if respuesta_2 == '1':
        print('>>>Debes permitirle una posición de suficiente ventilación')
        print('-'*80)
        print('Fin de las recomendaciones\n')
    else:
        print('>>>Debes administrar 5 ventilaciones y llamar a la Ambulancia')
        print('-'*80)
        llego_ambulancia = [' ', False, True] #Definimos una lista con buleanos para ciclo while
        valor = True #Inicializamos el valor de la sentencia while
        while valor:
            respuesta_3 = input('¿La persona presenta signos de vida? \n 1: SI \n 2: NO \nRespuesta: ')
            print('-'*80)
            if respuesta_3 == '1':
                print('>>>Tienes que reevaluar a la espera de la Ambulancia')
                print('-'*80)
            else:
                print('>>>Debes administrar Compresiones Torácicas hasta que llegue la ambulancia')
                print('-'*80)
            respuesta_4 = input('¿Llego la Ambulancia? \n 1: SI \n 2: NO \nRespuesta: ')
            valor = llego_ambulancia[int(respuesta_4)] #Reasigna valor segun la respuesta del usuario para ver si sale o no del ciclo dependiendo se llego o no la ambulancia
            print('-'*80)
        print('No hay más recomendaciones\n')
