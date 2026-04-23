# Sistema de Gestión de Inventario (CLI) 📦

Este es un sistema de gestión de inventario por línea de comandos (CLI) desarrollado en **Python** aplicando principios de **Programación Orientada a Objetos (POO)**. 

El proyecto simula la lógica de negocio real de un almacén técnico, diferenciando el trato entre activos retornables (herramientas) y bienes consumibles (insumos), manteniendo un registro de auditoría detallado de cada movimiento.

## 🚀 Características Principales

El sistema cuenta con un menú interactivo de 11 opciones que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) y lógicas de almacén:

* **Gestión de Catálogo:** Registro, edición, eliminación y búsqueda de materiales por código, nombre, marca o categoría.
* **Lógica de Negocio Diferenciada:**
    * **Herramientas:** Se gestionan bajo la lógica de préstamo y devolución. El sistema controla el stock dinámico y registra qué usuario tiene asignada la herramienta.
    * **Insumos:** Se gestionan bajo la lógica de consumo (retiro), descontando permanentemente el stock disponible.
* **Auditoría y Trazabilidad:** Cada acción (registro, préstamo, devolución, consumo) genera un log automático con fecha, hora, tipo de movimiento y persona responsable.
* **Ordenamiento y Reportes:** Listado de inventario ordenado por múltiples criterios y generación de reportes de historial completo por ítem.

## 🏗️ Estructura del Proyecto

El código está modularizado en tres archivos principales para separar las responsabilidades:

* `material.py`: Contiene el modelo de datos (Clase `Material`). Define los atributos base y el método de registro de movimientos (timestamps).
* `inventario.py`: Contiene el controlador lógico (Clase `Inventario`). Gestiona las colecciones de datos, las validaciones (Manejo de Excepciones) y las reglas de negocio para los préstamos e insumos.
* `main.py`: Punto de entrada de la aplicación. Maneja el bucle de la interfaz de consola y el menú interactivo para el usuario.

## 🛠️ Requisitos

* Python 3.x instalado en el sistema.
* No requiere librerías externas (solo utiliza módulos nativos como `datetime`).

## 💻 Instrucciones de Uso

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)
