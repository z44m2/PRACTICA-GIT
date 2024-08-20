class Paciente:
    def __init__(self):
        self.__nombre= " "
        self.__cedula= 0
        self.__genero= " "
        self.__servicio= " "

    def verNombre(self):
        return self.__nombre
    
    def verServicio(self):
        return self.__servicio
    
    def verGenero(self):
        return self.__genero
    
    def verCedula(self):
        return self.__cedula
    
    def asignarNombre(self, n):
        self.__nombre = n

    def asignarServicio(self, s):
        self.__servicio = s



    def asignarGenero(self, g):
        self.__genero = g

    def asignarCedula(self, c):
        self.__cedula = c

class Sistema:
    def __init__(self):
        self.__lista_pacientes = []
        self.__numero_pacientes = len(self.__lista_pacientes)

    def ingresarPaciente(self):
        nombre = input("Ingrese el nombre del paciente: ")
        cedula = int(input("Ingrese la cedula del paciente: "))
        genero = input("Ingrese el genero del paciente: ")
        servicio = input("Ingrese el servicio: ")
        p = Paciente()
        p.asignarNombre(nombre)
        p.asignarCedula(cedula)
        p.asignarGenero(genero)
        p.asignarServicio(servicio)
        self.__lista_pacientes.append(p)
        self.__numero_pacientes = len(self.__lista_pacientes)

    def verNumeroPacientes(self):
        return self.__numero_pacientes
    
    def verDatosPacientes(self):
        cedula = int(input("Ingrese la cédula a buscar: "))
        for paciente in self.__lista_pacientes:
            if cedula == paciente.verCedula():
                print("Nombre: " + paciente.verNombre())
                print("Cédula" + str(paciente.verNombre()))
                print("Género: " + paciente.verGenero())
                print("Servicio: " + paciente.verServicio())

my_sistem = Sistema()

while True:
    print("---------MENÚ---------\n1. Nuevo Paciente \n2. Numero de Pacientes \n3. Datos Paciente \n4. Salir")
    opcion = int(input("\nIngrese la opción deseada>>>>"))
    if opcion == 1:
        my_sistem.ingresarPaciente()

    elif opcion == 2:
        print("Actualmente se encuentran:" + str(my_sistem.verNumeroPacientes()) +"cantidad de pacientes.")

    elif opcion == 3:
        my_sistem.verDatosPacientes()

    elif opcion == 4:
        break
    
    else:
        print("Opcion invalida. \nPor favor intente de nuevo.")