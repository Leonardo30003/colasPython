from collections import deque

class GestorConsultas:
    def __init__(self):
        self.cola = deque()

    def nueva_consulta(self, consulta):
        self.cola.append(consulta)

    def atender_consulta(self):
        if self.cola:
            consulta = self.cola.popleft()
            print(consulta)
        else:
            print("No hay consultas pendientes.")

    def consultas_pendientes(self):
        return len(self.cola)
