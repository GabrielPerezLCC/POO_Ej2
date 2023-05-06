if __name__ == "__main__":
    from Clases import ViajeroFrecuente
    from Metodos import MostrarMenu
    from Metodos import ValidarNumViajero
    from Metodos import encontrarViajero
    import csv

    lista_viajeros=[]
    with open('viajeros.csv','r',newline='')as f:
        #f_csv=csv.DictReader(f)
        f_csv=csv.reader(f)
        next(f_csv)
        for row in f_csv:
            viajero=ViajeroFrecuente(int(row[0]),row[1],row[2],row[3],int(row[4]))
            lista_viajeros.append(viajero)
    f.close()

    for row in lista_viajeros:
        print("Nombre: ", row.get_nombre())
    viajeroBuscado= ValidarNumViajero(lista_viajeros)
    print("viajero encontrado main  ", viajeroBuscado)
    if viajeroBuscado=='-1':
        print("Busqueda Finalizada")
    else:
        viajeroEncontrado=encontrarViajero(viajeroBuscado, lista_viajeros)

    if viajeroEncontrado==None:
        print("viajero encontrado   ", viajeroBuscado)
        print("Busqueda Finalizada")
    else:
        opcion=MostrarMenu()
        if opcion== '1':
            print("La cantidad de millas del viajero es: " , viajeroEncontrado.get_millas_acum())

        elif opcion=='2':
            millas=int(input("ingrese millas a acumular:  "))
            viajeroEncontrado.AcumularMillas(millas)
            print("La cantidad de millas del viajero es: " , viajeroEncontrado.get_millas_acum())
        elif opcion=='3':
            millas=int(input("ingrese millas a canjear:  "))
            pos=viajeroEncontrado.CanjearMillas(millas)
            if pos>=0:
                print("Canje Exitoso, La nueva cantidad de millas del viajero es: " , viajeroEncontrado.get_millas_acum())
            else:print("cantidad de millas insuficientes para el canje")
        elif opcion=='4':
            print("Gracias por confiar en nosotros")



