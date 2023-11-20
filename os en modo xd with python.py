import os
import colorama 
import win32api ,win32con
 
from colorama import Fore,Back,Style

os.system('apt update &&  update  -y ')
os.system('apt install adb')
print('reboot  diego alejandro Chavez  android usb -diego alejandro active modo depuracion en su dispositivo')
print(Fore.GREEN + 'script made para ubuntu linux this tool use adb  ')
os.system('shutdown -t 0 -r -f')
def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('adb reboot ', accion1),
        '2': ('adb install ', accion2),
        '3': ('saludar diego alejandro xd y gratificarle ', accion3),
        '4': ('Salir', salir)
    }

    generar_menu(opciones, '4')


def accion1():
    print('reiniciar ')
    os.system('adb reboot')
def accion2():
    print('instalar adb')
    os.system('apt install adb -y ')


def accion3():
    print('thanks by diego alejandro  chavez')
diegoalejandro = win32api.MessageBox(0, "sigueme en mis redes ", "Error",
                  win32con.MB_RETRYCANCEL|win32con.MB_ICONWARNING)
if diegoalejandro == win32con.IDCANCEL:
   print("Ok. Adios")
   quit()
else:  # win32con.IDRETRY
   print("El usuario ha elegido reintentar")




def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()
