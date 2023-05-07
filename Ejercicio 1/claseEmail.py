import re, string, random

class Email:
    __idCuenta= ' '
    __dominio= ' '
    __tipoDominio= ' '
    __contraseña= ' '
    
    def __init__(self,idCuenta,dominio,tipoDom,contraseña):
        self.__idCuenta= idCuenta
        self.__dominio= dominio
        self.__tipoDominio= tipoDom
        self.__contraseña= contraseña
       
    def mostrarDatos(self):
        print(f"Id: {self.__idCuenta}\nDominio: {self.__dominio}\nTipo Dominio: {self.__tipoDominio}\nContraseña: {self.__contraseña}")
     
    def getDominio(self):
        dominio= self.__dominio
        return dominio
        
    def crearCuenta(self,correo):
        long_str= 10                    #variable que ayuda a la construccion de una contraseña
        aux= re.split(r'[@]',correo)    #genera una lista, cuyas componentes son los elementos de la cadena a separar por @
        part= re.split(r'[.]',aux[1])
        #linea 30 permite la construccion de una contraseña random
        #random.choice devuelve un elemento aleatorio de la secuencia ingresada como entrada
        #(en este caso string.ascii_letters y string.digits)
        #str.join une los elementos del iterable  
        contraseña= ''.join(random.choice(string.ascii_letters + string.digits)for _ in range(long_str))
        self.__init__(aux[0],part[0],part[1],contraseña)
        print("Cuenta creada con exito!")
        
    def modificar_contra(self,contraAct):
        if self.__contraseña == contraAct:
            nueva= input("Ingrese una nueva contraseña: ")
            self.__contraseña= nueva
        else: print("La contraseña ingresada no coincide con la registrada")
        