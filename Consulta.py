class Consulta:
    def __init__(self, nombre, correo, mensaje):
        self.nombre = nombre
        self.correo = correo
        self.mensaje = mensaje

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_correo(self):
        return self.correo

    def set_correo(self, correo):
        self.correo = correo

    def get_mensaje(self):
        return self.mensaje

    def set_mensaje(self, mensaje):
        self.mensaje = mensaje

    def __str__(self):
        return "Consulta{nombre=" + self.nombre + ", correo=" + self.correo + ", mensaje=" + self.mensaje + "}"
