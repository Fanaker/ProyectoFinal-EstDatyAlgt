from inventario import Inventario

def menu():
    inventario = Inventario()
    inventario.materiales_datos()

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar nuevo material")
        print("2. Listar materiales")
        print("3. Buscar material por código")
        print("4. Editar material")
        print("5. Eliminar material")
        print("6. Registrar préstamo de herramienta")
        print("7. Registrar devolución de herramienta")
        print("8. Consultar quién tiene una herramienta")
        print("9. Registrar uso de insumo")
        print("10. Historial de movimientos de herramienta")
        print("11. Historial completo")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            inventario.agregar_material()
        elif opcion == "2":
            inventario.ordenar_materiales()
        elif opcion == "3":
            inventario.buscar_material()
        elif opcion == "4":
            inventario.editar_material()
        elif opcion == "5":
            inventario.eliminar_material()
        elif opcion == "6":
            inventario.prestar_herramienta()
        elif opcion == "7":
            inventario.devolver_herramienta()
        elif opcion == "8":
            inventario.consultar_responsable()
        elif opcion == "9":
            inventario.registrar_retiro_insumo()
        elif opcion == "10":
            inventario.historial_material()
        elif opcion == "11":
            inventario.reporte_total()
        elif opcion == "0":
            print("Gracias por usar el sistema de inventario.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
