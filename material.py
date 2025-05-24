class Material:
    def __init__(self, codigo, nombre, categoria, cantidad, marca):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria  # Herramienta o Insumo
        self.cantidad = cantidad
        self.marca = marca
        self.prestamos = []  # Lista de personas que tienen una herramienta prestada
        self.historial = []  # Lista de acciones

    def mostrar(self):
        if self.cantidad == 0:
            if self.categoria.lower() == "herramienta":
                estado = "Prestada"
            else:
                estado = "Agotado"
        else:
            estado = "Disponible"
        print(f"Código: {self.codigo} | Nombre: {self.nombre} | Categoría: {self.categoria} | Cantidad: {self.cantidad} | Marca: {self.marca} | Estado: {estado}")

    def registrar_movimiento(self, tipo, persona=None):
        from datetime import datetime
        ahora = datetime.now()
        registro = {
            "fecha": ahora.strftime("%Y-%m-%d"),
            "hora": ahora.strftime("%H:%M:%S"),
            "tipo": tipo,
        }
        if persona:
            registro["persona"] = persona
        self.historial.append(registro)
