from random import choice

rutaPreguntas = "Preguntas.txt"
#########################################
def VerificarClave(con):
    with open ("Acceso.txt", "r") as archivo:
        texto = archivo.readlines()
    if texto[0] == con:
        return OpcionesAdministrativas()
    else:
        print ("Clave acceso es incorrecta\n")
        return MenuPrincipal()

def MenuPrincipal():
    print ("==OPCIONES PRINCIPALES DEL JUEGO==")
    print ("1: Opciones Administrativas")
    print ("2: Opciones de Jugador")
    print ("3: Salir\n")

    opcion = input ("Digite la opcion que desea realizar:")
    
    
    if opcion == '1':
        con = input ("Clave de acceso para ingresar:")
        return VerificarClave(con)

    elif opcion == '2':
        pass

    elif opcion == '3':
        print ("HAS SALIDO COMPLETAMENTE DEL PROGRAMA Y NO SERAS MILLONARIO")
    else:
        print ("Opcion no existe, ingrese una opcion valida\n")
        MenuPrincipal()
    
#################################################################
'''
Solo lee archivo y convierte lista a listas
'''
def obtenerContenidoArchivo(nombre):
    with open(nombre,'r') as archivo:
        todoTexto = archivo.read()
    convertirTextoaLista = todoTexto.split("\n")
    return convierteaLista(convertirTextoaLista)

def convierteaLista(lista):
    if lista == []:
        return []
    elif lista[0] != "":
        return [lista[0].split(",")] + convierteaLista(lista[1:])

    else:
        return convierteaLista(lista[1:])


#################################################################
'''
#Opcion 1 de menu principal
'''
def OpcionesAdministrativas():
    print ("\n ==Menu Administrativo==")
    print ("1: Gestion de Preguntas y Respuestas")
    print ("2: Gestion de Juegos")
    print ("3: Historial de Juegos")
    print ("4: Estadisticas de Juegos")
    print ("5: Retornar")

    opcion = input ("Digite la opcion que desea realizar: ")

    if opcion == '1':
        return menuPreguntas()
        
            
    if opcion == '5':
        MenuPrincipal()
    else:
        OpcionesAdministrativas()

def menuPreguntas():
    print ("\n ##Menú Gestion de Preguntas y Respuestas##")
    print ("1: Incluir pregunta")
    print ("2: Eliminar pregunta")
    print ("3: Modificar pregunta")
    print ("4: Mostrar preguntas pregunta")
    print ("5: Retornar")

    op = input ("Digite la opcion que desea realizar: ")

    if op == '1':
        IncluirPregunta()

    if op == '2':
        EliminarPregunta()

    if op == '3':
        ModificarPregunta()

    if op == '4':
        MostrarPreguntas("Preguntas.txt")
        menuPreguntas()

    if op == '5':
        OpcionesAdministrativas()
    else:
        menuPreguntas()
#funciones opcion 1 menu de gestion pyr
def IncluirPregunta():
    print ("Incluya una nueva pregunta: ")
    add =  input ("")
    original = obtenerContenidoArchivo(rutaPreguntas)
    if existePregunta(original,add):
        print ("¡La pregunta ya existe!\n")
        return OpcionesAdministrativas()
    else:
        mostrar = original[-1][0].split(',')
        cod = int(mostrar[0]) + 1
        pas = str (cod)

        print ("Incluya las respuestas: ")
        answer1 = input ("")
        answer2 = input ("")
        answer3 = input ("")
        answer4 = input ("")

        # indice, pregunta, rep1, rep2, res3, res4(Corrct)
        linea =  (pas + ','+add+","+ answer1+','+ answer2+',' + answer3+',' + answer4+"\n")
        print ("¡Preguntas y respuestas añadidas correctamente! \n")
        escribirArchivo_V2("Preguntas.txt", linea)
        OpcionesAdministrativas()
        
def MostrarPreguntas(nombre):
    with open(nombre,'r') as archivo:
        todoTexto = archivo.read()
    convertirTextoaLista = todoTexto.split("\n")
    imprimirPreguntas()

def escribirArchivo_V2(nombreArchivo, mensaje):
    file = open("Preguntas.txt", 'a') #append
    file.write(mensaje)
    file.close()

def existePregunta(lista,add):
    if lista != []:
        pregunta = lista[0][1]
        if pregunta.lower() == add.lower():
            return True
        else:
            return existePregunta(lista[1:],add)
    else:
        return False
    

#funciones opcion 2 menu de pyr

def EliminarPregunta():
    preguntas= obtenerContenidoArchivo("Preguntas.txt")
    MostrarPreguntas("Preguntas.txt")
    print ("Cual pregunta desea eliminar?: ")
    num = input ("")
    print("Se eliminara la: " + num)
    archivo=open("Preguntas.txt","w")
    archivo.close()
    EliminarPregunta_Aux(preguntas, num)

def EliminarPregunta_Aux(lista,num):
    if lista == []:
        print ("¡Pregunta eliminada exitosamente!\n")
        return menuPreguntas()
    if lista[0][0] == num:
        return EliminarPregunta_Aux(lista[1:] ,num)
    else:
        pregunta = lista[0]
        linea= (str(pregunta[0]) + ','+ str(pregunta[1])+","+ str(pregunta[2])+','+ str(pregunta[3])+',' + str(pregunta[4])+',' + str(pregunta[5])+"\n")
        escribirArchivo_V2("Preguntas.txt", linea)
        return EliminarPregunta_Aux(lista[1:] ,num)

    
#######################################################

def ModificarPregunta():
    preguntas= obtenerContenidoArchivo("Preguntas.txt")
    MostrarPreguntas("Preguntas.txt")
    print ("Cuál pregunta desea modificar?: ")
    num = input ("")
    print("Se modificará la pregunta: " + num)
    print ("Escriba la nueva pregunta: ")
    add =  input ("")
    original = obtenerContenidoArchivo(rutaPreguntas)
    if existePregunta(original,add):
        print ("¡La pregunta ya existe, no se puede modificar por la nueva!\n")
        return OpcionesAdministrativas()
    else:
        print ("Incluya las respuestas: ")
        answer1 = input ("")
        answer2 = input ("")
        answer3 = input ("")
        answer4 = input ("")
        archivo=open("Preguntas.txt","w")
        archivo.close()
        ModificarPregunta_Aux(preguntas, num, add, answer1, answer2, answer3, answer4)

def ModificarPregunta_Aux(lista,num, add, answer1, answer2, answer3, answer4):
    if lista == []:
        print ("¡Preguntas y respuestas modificadas correctamente! \n")
        return menuPreguntas()
    if lista[0][0] == num:
        linea =  (str(num)+','+add+","+ answer1+','+ answer2+',' + answer3+',' + answer4+"\n")
        print("Correcta: "+ linea)
        escribirArchivo_V2("Preguntas.txt", linea)
        return ModificarPregunta_Aux(lista[1:] ,num, add, answer1, answer2, answer3, answer4)
    else:
        pregunta = lista[0]
        linea= (str(pregunta[0]) + ','+ str(pregunta[1])+","+ str(pregunta[2])+','+ str(pregunta[3])+',' + str(pregunta[4])+',' + str(pregunta[5])+"\n")
        escribirArchivo_V2("Preguntas.txt", linea)
        return ModificarPregunta_Aux(lista[1:] ,num, add, answer1, answer2, answer3, answer4)

#######################################################
    
def imprimirPreguntas():
    listaPreguntas = obtenerContenidoArchivo(rutaPreguntas)
    print (cascada(listaPreguntas))
    

'''
hacer mi pregunta hacia abajo
'''
def cascada(lista):
    if lista == []:
        print ("\n")
    else:
        print (lista[0])
        return cascada(lista[1:])
#######################################################

MenuPrincipal()
