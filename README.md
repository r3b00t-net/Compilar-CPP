# Compilador Multi-Lenguaje

Este proyecto proporciona un script en Python que permite compilar archivos en C, C++, y C# utilizando `gcc`, `g++`, y `msc` respectivamente. El script está diseñado para ser flexible y fácil de usar, facilitando la compilación de diferentes tipos de archivos de código fuente desde una única interfaz.

## Características

- **Compatibilidad Multi-Lenguaje**: Compila archivos en C, C++, y C#.
- **Flexibilidad**: Usa `gcc`, `g++`, y `msc` para la compilación según el tipo de archivo.
- **Automatización**: Simplifica el proceso de compilación con un único script.

## Requisitos

- Python 3.x
- Compiladores:
  - `gcc` para archivos C
  - `g++` para archivos C++
  - `msc` para archivos C#

## Instalación

1. Clona este repositorio:
    ```sh
    git clone https://github.com/tu-usuario/compilador-multi-lenguaje.git
    ```
2. Navega al directorio del proyecto:
    ```sh
    cd compilador-multi-lenguaje
    ```

## Uso

1. Asegúrate de tener los compiladores necesarios instalados en tu sistema y accesibles desde la línea de comandos.
2. Ejecuta el script de compilación proporcionando el archivo fuente como argumento:
    ```sh
    python compilar.py archivo_fuente.c
    ```

   El script determinará automáticamente el tipo de archivo y utilizará el compilador adecuado.

## Ejemplos

Compilar un archivo C:
```sh
python compilar.py ejemplo.c
