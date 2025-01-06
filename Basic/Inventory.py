##############################################################################
# Aplicación que permita agregar, eliinar y buscar productos en un invetario #
##############################################################################

def menu() -> str: 
    print("-----------------------------------------------------------------------")
    print("0: Ver productos\n1: Agregar producto\n2: Eliminar producto\n3: Salir")
    print("-----------------------------------------------------------------------")
    accion = input("Bienvenido! Indique a continuacion que desea realizar: ")
    
    return accion

def accion() -> str:
    print("\nCategorias:\n|| Frutas || Carnes || Pescados || Otros ||")
    producto = input("> Indique que categoria desea actualizar: ")

    while (producto != "Frutas" and producto != "Carnes" and producto != "Pescados" and producto != "Otros"):
        print("\t-> Categoria no valida, pruebe otra vez.")
        print("\nCategorias:\n|| Frutas || Carnes || Pescados || Otros ||")
        producto = input("> Indique que categoria desea actualizar: ")
    
    return producto

frutas = list(); carnes = list(); pescados = list(); otros = list()
sistema = dict({"Frutas": frutas, 
               "Carnes": carnes, 
               "Pescados": pescados, 
               "Otros": otros})

opcion = menu()
while(opcion != '3'):

    if opcion == '0':# Visualizar almacenamiento
        
        print("##################\n# Almacenamiento #\n##################\n")
        print(sistema)


    elif opcion == '1':# Agregar producto

        producto = accion()

        tipo = input(f"\t> Producto que desea añadir a <{producto}>: ")

        try:
            if(sistema[producto].index(tipo) >= 0):# Existe el elemento en la lista
                print(f"\t\t> El producto <{tipo}> ya se encuentra registarado en <{producto}>.")
            
        except ValueError:# -> Este error salta en index si no encuentra la palabra o si esta vacia la lista
            sistema[producto].append(tipo)
            print("\t\t> Producto añadido correctamente.")
        
    elif opcion == '2':# Eliminar producto
        
        producto = accion()

        tipo = input(f"\t> Producto que desea eliminar de <{producto}>: ")

        try:
            sistema[producto].remove(tipo) 
            print("\t\t> Producto eliminado correctamente.")

        except ValueError:# -> Este error salta si no existe el elemento en la lista.
            print(f"\t\t> El producto <{tipo}> no se ha encontrado en la categoria <{producto}>")      

    else:
        print(f"\t> La solicitud <{opcion}> no es válida.")


    opcion = menu()


