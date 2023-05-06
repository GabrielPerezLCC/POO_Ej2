from Clases import ViajeroFrecuente
def MostrarMenu():
        opcion=None
        while opcion not in['1','2','3','4']:
            try:
                print("Menú de opciones:")
                print("1- Consultar Cantidad de Millas.")
                print("2- Acumular Millas.")
                print("3- Canjear Millas.")
                print("4- Salir")    
                opcion=input("Elija la opcion Deseada ")
                
            except ValueError:
                print("elija una opcion correcta")
        
        return opcion

def ValidarNumViajero(lista_viajeros):
    encontrado= None
    detener_busqueda= False

    while encontrado is None and not detener_busqueda:

        num_viaj=(input("Ingrese el numero de Viajero a Buscar, cero para terminar: "))
        if num_viaj == '0':
                 encontrado=-1
                 detener_busqueda=True
                 print("detener", detener_busqueda)
                 
        else:
            
            try:
                 num_viaj=int(num_viaj)  
                 encontrado=num_viaj  
                 print("encontrado es ", encontrado)
            except ValueError:
                 print("Ingrese un dato numerico  ")
                 continue
    
    return encontrado
        
            

def encontrarViajero(viajeroBuscado, lista_viajeros):
    
    encontrado=None
    seguir=True
    while encontrado==None and seguir:
        encontrado=ViajeroFrecuente().BuscarViajero(viajeroBuscado,lista_viajeros)
        if encontrado is None:
            O=input("desea seguir buscando N para detener S para continuar ").upper()
            if O=="S":
                 
                viajeroBuscado=ValidarNumViajero(lista_viajeros)
            else:
                if O=="N":
                      seguir=False
                      encontrado=None
                      
                else:
                    print("ingrese la opcion correcta")
                    continue
      
    return encontrado