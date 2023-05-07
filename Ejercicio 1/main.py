from claseEmail import Email as e 
import csv

"""#-----------------------CARGA---------------------------
def cargaDatos(lista):
    print("Ingrese los siguientes datos: ")
    id= input("Id: ")
    dominio= input("Dominio: ")
    tipoDominio= input("Tipo de dominio: ")
    contraseña= input("Contraseña: ")
    un_Email= e(id,dominio,tipoDominio,contraseña)
    lista.append(un_Email)                  #agrega un elemento a la lista"""

#----------------CREACION DE UN OBJETO A PARTIR DE UN CORREO, MOSTRANDO UN MENSAJE FORMAL PUNTO 1---------------------
def crearInstancia_email(lista):
    otroEmail= e('','','','')
    nombre= input("Ingrese su nombre: ")
    correo= input("Ingrese su dirección de correo: ")
    otroEmail.crearCuenta(correo)
    lista.append(otroEmail)
    print(f"Estimado {nombre} te enviaremos tus mensajes a la dirección {correo}")

#---------------MODIFICACION DE CONTRASEÑA PUNTO 2--------------------    
def modificar_contraseña(lista): 
    print("Modificacion de contraseña")
    actual= input("Ingrese la contraseña actual:")
    for object in lista:  
        object.modificar_contra(actual)
    print("Contraseña modificada con exito!")
    
#-------CREACION DE UN OBJETO A PARTIR DE UN CORREO PUNTO 3--------
def crear_obj(lista):
    print("Creacion de una cuenta")
    print("Ingrese los siguientes datos: ")
    correo= input("Direccion de correo: ")
    otro_email= e("","","","")
    otro_email.crearCuenta(correo)
    lista.append(otro_email)

#-------------------LECTURA DE UN ARCHIVO CSV PARA CREAR OBJETOS A PARTIR DE UN CORREO PUNTO 4----------------------
def verif_y_crearCuenta(lista):
    with open("datosPrueba.csv") as archivo:
        reader= csv.reader(archivo,delimiter=';')
        for fila in reader:
            condicion= fila[0].find('@') #devuelve -1 si no encontro el caracter a buscar en la subcadena
            #print(fila)
            if condicion != -1:
                condicion2= fila[0].find('.')
                if condicion2 != -1:
                    tercerEmail= e("","","","")
                    tercerEmail.crearCuenta(fila[0])
                    lista.append(tercerEmail)
                else: print(f"No es posible crear una cuenta para {fila[0]} porque es una direccion no valida")
            else: print(f"No es posible crear una cuenta para {fila[0]} porque es una direccion no valida")    
    archivo.close()

#--------------CALCULA LA CANTIDAD DE OBJETOS QUE TIENEN EL MISMO DOMINIO INCISO b) PUNTO 4-----------------
def comparacionDominio(lista):
    print("Punto 4 inciso b)")
    dominio= input("Ingrese un dominio para ver cuantos Emails tienen el mismo: ")
    cont=0
    for object in lista:
        if dominio==object.getDominio():
            cont+=1
    print(f"{cont} Emails tienen el dominio {dominio}")


#---------------PROGRAMA PRINCIPAL------------------
if __name__=='__main__':
    lista_emails= []
    #cargaDatos(lista_emails)
    crearInstancia_email(lista_emails)
    modificar_contraseña(lista_emails)
    crear_obj(lista_emails)
    verif_y_crearCuenta(lista_emails)
    comparacionDominio(lista_emails)