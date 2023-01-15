#
# clave = "kerlys123"
# clave_secundaria = "123kerlys"
# clave_usuario = input()
#
# if clave == clave_usuario:
#     print("BIENVENIDO, CLAVE CORRECTA")
#
# elif clave_secundaria == clave_usuario:
#     print("BIENVENIDO, CLAVE SECUNDARIA CORRECTA")
#
# else:
#     print("ACCESO DENEGADO, LLAMANDO A LA POLICIA")


edad_min_carro = 18
edad_kerlys = int(input())

if edad_kerlys <= edad_min_carro:
    print("PUEDES ADQUIRIR UN CARRO")
else:
    print("NO PUEDES TENER UN CARRO, ERES DEMASIADO JOVEN")
