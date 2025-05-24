from material import Material

class Inventario:
    def __init__(self):
        self.materiales = []

    #Metodo 1: Para agregar materiales
    def agregar_material(self):
        while True:
            codigo = input("Ingrese el código: ")
            if self.buscar_material_por_codigo(codigo):
                print("Ya existe un material con ese código. Intenta con otro.")
            else:
                break

        nombre = input("Ingrese el nombre: ")

        # Para validar categoría
        while True:
            categoria = input("Ingrese la categoría (Herramienta/Insumo): ").strip().capitalize()
            if categoria in ["Herramienta", "Insumo"]:
                break
            print("Categoría no válida. Debe ser 'Herramienta' o 'Insumo'.")

        # Para validar cantidad
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad: "))
                if cantidad < 0:
                    raise ValueError
                break
            except ValueError:
                print("La cantidad debe ser un número entero positivo.")

        marca = input("Ingrese la marca: ")

        nuevo = Material(codigo, nombre, categoria, cantidad, marca)
        self.materiales.append(nuevo)
        nuevo.registrar_movimiento("registro")
        print("Material registrado correctamente.")

    #Metodo 2: Para ordenar los materiales por...
    def ordenar_materiales(self):
        print("Opciones para ordenar materiales:")
        print("1. Por código")
        print("2. Por nombre (alfabético)")
        print("3. Por categoría (Herramienta/Insumo)")
        print("4. Por orden de registro")
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            ordenados = sorted(self.materiales, key=lambda m: m.codigo.lower())
        elif opcion == "2":
            ordenados = sorted(self.materiales, key=lambda m: m.nombre.lower())
        elif opcion == "3":
            ordenados = sorted(self.materiales, key=lambda m: m.categoria.lower())
        elif opcion == "4":
            ordenados = self.materiales
        else:
            print("Opción no válida.")
            return

        if ordenados:
            for m in ordenados:
                m.mostrar()
        else:
            print("No hay materiales para listar.")


    #Metodo 3: Para buscar material por...
    def buscar_material(self):
        print("\nOpciones de búsqueda:")
        print("1. Código")
        print("2. Nombre")
        print("3. Marca")
        print("4. Categoría (H para herramienta, I para insumo)")
        opcion = input("Seleccione una opción (1-4): ")
        termino = input("Ingrese el término de búsqueda: ").strip().lower()
        encontrados = []

        for material in self.materiales:
            if opcion == "1" and termino in material.codigo.lower():
                encontrados.append(material)
            elif opcion == "2" and termino in material.nombre.lower():
                encontrados.append(material)
            elif opcion == "3" and termino in material.marca.lower():
                encontrados.append(material)
            elif opcion == "4":
                if termino == "h" and material.categoria.lower() == "herramienta":
                    encontrados.append(material)
                elif termino == "i" and material.categoria.lower() == "insumo":
                    encontrados.append(material)

        if encontrados:
            print(f"\nMateriales encontrados:")
            for m in encontrados:
                m.mostrar()
        else:
            print("No se encontraron materiales con ese criterio.")

    def buscar_material_por_codigo(self, codigo):
        codigo = codigo.lower()
        for material in self.materiales:
            if material.codigo.lower() == codigo:
                return material
        return None


    #Metodo 4: Para editar los datos de un material
    def editar_material(self):
        codigo = input("Ingrese el código del material a editar: ")
        material = self.buscar_material_por_codigo(codigo)
        if material:
            print("Ingrese los nuevos valores (presione Enter para mantener):")
            nombre = input(f"Nombre ({material.nombre}): ")
            categoria = input(f"Categoría ({material.categoria}): ")
            cantidad = input(f"Cantidad ({material.cantidad}): ")
            marca = input(f"Marca ({material.marca}): ")

            if nombre:
                material.nombre = nombre
            if categoria:
                material.categoria = categoria
            if cantidad:
                try:
                    material.cantidad = int(cantidad)
                except ValueError:
                    print("Cantidad inválida. Debe ser un número entero.")

            if marca:
                material.marca = marca

            print("Material actualizado correctamente.")
            self.generar_reportes(material)
        else:
            print("Material no encontrado.")


    #Metodo 5: Para eliminar un material de la lista
    def eliminar_material(self):
        codigo = input("Ingrese el código del material a eliminar: ")
        material = self.buscar_material_por_codigo(codigo)
        if material:
            self.materiales.remove(material)
            print("Material eliminado correctamente.")
            self.generar_reportes(material)
        else:
            print("Material no encontrado.")


    #Metodo 6: Para clasificar una herramienta como prestada.
    def prestar_herramienta(self):
        codigo = input("Ingrese el código de la herramienta a prestar: ")
        persona = input("Ingrese el nombre de la persona: ")
        material = self.buscar_material_por_codigo(codigo)

        if material and material.categoria.lower() == "herramienta":
            if material.cantidad > 0:
                material.prestamos.append(persona)
                material.cantidad -= 1
                material.registrar_movimiento("préstamo", persona)
                print("Herramienta prestada correctamente.")
                self.generar_reportes(material)
            else:
                print("No hay unidades disponibles para préstamo.")
        else:
            print("Herramienta no encontrada o no válida.")


    #Metodo 7: Para clasificar a una herramienta devuelta como disponible
    def devolver_herramienta(self):
        codigo = input("Ingrese el código de la herramienta a devolver: ")
        persona = input("Ingrese el nombre de la persona que devuelve: ")
        material = self.buscar_material_por_codigo(codigo)

        if material and material.categoria.lower() == "herramienta":
            if persona in material.prestamos:
                material.prestamos.remove(persona)
                material.cantidad += 1
                material.registrar_movimiento("devolución", persona)
                print("Herramienta devuelta correctamente.")
                self.generar_reportes(material)
            else:
                print("Esta persona no tiene esta herramienta prestada.")
        else:
            print("Herramienta no encontrada o no válida.")

    #Metodo 8: Para ver quién tiene la(s) herramienta(s)
    def consultar_responsable(self):
        codigo = input("Ingrese el código de la herramienta: ")
        material = self.buscar_material_por_codigo(codigo)

        if material and material.categoria.lower() == "herramienta":
            if material.prestamos:
                print(f"Unidades prestadas de '{material.nombre}':")
                for persona in material.prestamos:
                    print(f" - {persona}")
            else:
                print("La herramienta no está prestada actualmente.")
        else:
            print("Herramienta no encontrada o no válida.")

    #Metodo 9: Para registrar el uso de un insumo, estos ya no se devuelven, solo se restan
    def registrar_retiro_insumo(self):
        codigo = input("Código del insumo: ")
        material = self.buscar_material_por_codigo(codigo)
        if material:
            if material.categoria.lower() == "insumo":
                cantidad = int(input("Cantidad a retirar: "))
                if cantidad <= 0:
                    print("La cantidad debe ser mayor que cero.")
                    return
                if cantidad <= material.cantidad:
                    persona = input("Nombre de quien retira: ")
                    material.cantidad -= cantidad
                    material.registrar_movimiento("Retiro de insumo", persona)
                    print("Retiro registrado correctamente.")
                    self.generar_reportes(material)
                else:
                    print("Cantidad insuficiente en stock.")
            else:
                print("Este material no es un insumo.")
        else:
            print("Material no encontrado.")

    #Metodo 10: Para ver el historial de movimientos de un material.
    def historial_material(self):
        codigo = input("Ingrese el código del material: ")
        material = self.buscar_material_por_codigo(codigo)
        if material:
            print(f"\nHistorial del material: {material.nombre}:")
            for reg in material.historial:
                print(reg)
        else:
            print("Material no encontrado.")


    def generar_reportes(self, material):
        if not material.historial:
            print("No hay historial para generar un reporte.")
            return

        opcion = input("¿Desea generar un reporte de esta acción? (s/n): ")
        if opcion.lower() == "s":
            ultimo = material.historial[-1]
            print("\n--- REPORTE DE ACCIÓN ---")
            print(f"Código: {material.codigo}")
            print(f"Nombre: {material.nombre}")
            print(f"Categoría: {material.categoria}")
            print(f"Marca: {material.marca}")
            print(f"Cantidad disponible: {material.cantidad}")
            print("Historial reciente:")
            tipo = ultimo['tipo'].capitalize()
            fecha = ultimo['fecha']
            hora = ultimo['hora']
            persona = ultimo.get('persona', 'N/A')
            if persona != 'N/A':
                print(f"  {fecha} {hora} - {tipo} - Persona: {persona}")
            else:
                print(f"  {fecha} {hora} - {tipo}")
            print("--------------------------\n")


    def reporte_total(self):
        print("\n--- REPORTE DE INVENTARIO ---")
        for material in self.materiales:
            print(f"Código: {material.codigo}")
            print(f"Nombre: {material.nombre}")
            print(f"Categoría: {material.categoria}")
            print(f"Cantidad disponible: {material.cantidad}")
            print(f"Marca: {material.marca}")
            print("Historial:")
            if material.historial:
                for h in material.historial:
                    tipo = h['tipo'].capitalize()
                    fecha = h['fecha']
                    hora = h['hora']
                    persona = h.get('persona', 'N/A')
                    if persona != 'N/A':
                        print(f"  {fecha} {hora} - {tipo} - Persona: {persona}")
                    else:
                        print(f"  {fecha} {hora} - {tipo}")
            else:
                print("  Sin movimientos registrados.")
            print("-" * 30)



    def materiales_datos(self):
        m = Material("P01", "martillo", "herramienta", 3, "Stanley")
        m.registrar_movimiento("registro")
        self.materiales.append(m)
        m = Material("P08", "sensores", "insumo", 20, "Sew")
        m.registrar_movimiento("registro")
        self.materiales.append(m)
        m = Material("P11", "variadores", "insumo", 10, "ABB")
        m.registrar_movimiento("registro")
        self.materiales.append(m)
        m = Material("P02", "taladro", "herramienta", 1, "Bosch")
        m.registrar_movimiento("registro")
        self.materiales.append(m)
        m = Material("P09", "fusibles", "insumo", 40, "Omron")
        m.registrar_movimiento("registro")
        self.materiales.append(m)
        m = Material("P04", "amperímetro", "herramienta", 1, "Fluke")
        m.registrar_movimiento("registro")
        self.materiales.append(m)
        m = Material("P10", "tornillos", "insumo", 200, "Generico")
        m.registrar_movimiento("registro")
        self.materiales.append(m)
        m = Material("P05", "detector", "herramienta", 1, "Generico")
        m.registrar_movimiento("registro")
        self.materiales.append(m)
        m = Material("P06", "pinza", "herramienta", 1, "Generico")
        m.registrar_movimiento("registro")
        self.materiales.append(m)
        m = Material("P03", "alicate", "herramienta", 1, "Stanley")
        m.registrar_movimiento("registro")
        self.materiales.append(m)
        m = Material("P07", "amoladora", "herramienta", 1, "Bosch")
        m.registrar_movimiento("registro")
        self.materiales.append(m)