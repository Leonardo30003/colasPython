class Consulta:
    def __init__(self, nombre, correo, consulta):
        self.nombre = nombre
        self.correo = correo
        self.consulta = consulta

    def __str__(self):
        return f"Consulta{{nombre={self.nombre}, correo={self.correo}, consulta={self.consulta}}}"


class GestorConsultas:
    def __init__(self):
        self.cola = []

    def nueva_consulta(self, consulta):
        self.cola.append(consulta)

    def atender_consulta(self):
        if self.cola:
            consulta = self.cola[0]
            print(consulta)
            self.cola.pop(0)
        else:
            print("No hay consultas pendientes.")

    def consultas_pendientes(self):
        return len(self.cola)


gestor = GestorConsultas()
for _ in range(5):
    print("Ingresa tu nombre:")
    nombre = input()
    print("Ingresa tu correo:")
    correo = input()
    print("Ingresa el motivo de tu consulta:")
    consulta = input()
    gestor.nueva_consulta(Consulta(nombre, correo, consulta))

print("Existen", gestor.consultas_pendientes(), "consultas pendientes")
while gestor.consultas_pendientes() > 0:
    print("Si desea atender la consulta, presione 1")
    bandera = input()
    if bandera == "1":
        gestor.atender_consulta()
        print("Existen", gestor.consultas_pendientes(), "consultas pendientes")
