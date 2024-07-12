import os
import sys
import shutil

def check_installation(tool_name, install_command):
    if shutil.which(tool_name) is None:
        print(f"Error: {tool_name} no está instalado.")
        print(f"Por favor, instale {tool_name} ejecutando: {install_command}")
        sys.exit(1)

# Verificar si mingw y mcs están instalados
check_installation("x86_64-w64-mingw32-gcc", "sudo apt-get install mingw-w64")
check_installation("x86_64-w64-mingw32-g++", "sudo apt-get install mingw-w64")
check_installation("mcs", "sudo apt-get install mono-mcs")

print("██████╗░██████╗░██████╗░░█████╗░░█████╗░████████╗")
print("██╔══██╗╚════██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝")
print("██████╔╝░█████╔╝██████╦╝██║░░██║██║░░██║░░░██║░░░")
print("██╔══██╗░╚═══██╗██╔══██╗██║░░██║██║░░██║░░░██║░░░")
print("██║░░██║██████╔╝██████╦╝╚█████╔╝╚█████╔╝░░░██║░░░")
print("╚═╝░░╚═╝╚═════╝░╚═════╝░░╚════╝░░╚════╝░░░░╚═╝░░░")

print("""Ingrese el tipo de compilacion:
                1 [*] Archivo C#
                2 [*] Archivo C
                3 [*] Archivo C++
                4 [*] Salir""")

options = input("Ingrese su opcion: ")

def compile_csharp():
    csharp = input("Ingrese el nombre del archivo: ")
    os.system(f"mcs -out:salida.exe {csharp}")
    print("Archivo Compilado en salida.exe")

def compile_c():
    c = input("Ingresa el nombre del archivo: ")
    os.system(f"x86_64-w64-mingw32-gcc -o salida2.exe {c}")
    print("Archivo Compilado en salida2.exe")

def compile_cpp():
    cpp = input("Ingresa el nombre del archivo: ")
    os.system(f"x86_64-w64-mingw32-g++ -std=c++17 -o salida3.exe {cpp} -lstdc++fs")
    print("Archivo Compilado en salida3.exe")

if options == '1':
    compile_csharp()

elif options == '2':
    compile_c()

elif options == '3':
    compile_cpp()

elif options == '4':
    print("Usted salio del Script")
    sys.exit()
else:
    print("Ingrese uno de esos numeros!")
    sys.exit()

