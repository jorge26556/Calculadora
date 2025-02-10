# 🖩 Calculadora con Interfaz Gráfica (Tkinter)

## 📌 Descripción
Este proyecto es una calculadora gráfica desarrollada en **Python** utilizando la librería **Tkinter**.  
Cuenta con funciones matemáticas básicas como **suma, resta, multiplicación, división y porcentaje**, además de opciones para **borrar, retroceder y apagar**.  

## 🎨 Características
- **Interfaz gráfica** intuitiva y fácil de usar.
- **Soporte para operaciones con porcentajes** (ej. `100+10%` se convierte automáticamente en `100+(100*(10/100)) = 110`).
- **Botón de retroceso (←)** para corregir errores sin necesidad de borrar toda la expresión.
- **Soporte para números decimales**.
- **Diseño visual atractivo**, con colores diferenciados para operadores y números.
- **Opción de salir de la aplicación** con el botón **EXIT**.

## 🖥️ Captura de pantalla (Ejemplo)
📌 *(Puedes agregar aquí una imagen de la interfaz gráfica de la calculadora)*

## 📦 Instalación y Uso
### 1️⃣ Requisitos previos
Asegúrate de tener **Python 3.x** instalado en tu sistema. Puedes verificarlo con el siguiente comando:
python --version

2️⃣ Clonar o descargar el repositorio
Puedes clonar este repositorio usando Git o descargar el archivo manualmente:

git clone https://github.com/tu_usuario/calculadora-tkinter.git
cd calculadora-tkinter

3️⃣ Ejecutar la calculadora
Ejecuta el script con el siguiente comando:

python calculadora.py

Si usas Windows, puedes hacer doble clic en el archivo calculadora.py.

⚙️ Tecnologías utilizadas
Python (Lenguaje de programación)
Tkinter (Para la interfaz gráfica)
Expresiones regulares (re) (Para manejo avanzado de operaciones con porcentajes)

✨ Funcionalidades
Botón	- Función
+ - * /	Operaciones matemáticas básicas
%	Calcula porcentajes de manera inteligente
=	Evalúa la expresión ingresada
C	Borra toda la entrada
←	Borra el último carácter ingresado
EXIT	Cierra la aplicación

🛠️ Mejoras futuras
Implementación de un historial de cálculos.
Agregar soporte para más funciones matemáticas (raíz cuadrada, exponenciales, etc.).
Permitir personalización de la interfaz con diferentes temas de color.
