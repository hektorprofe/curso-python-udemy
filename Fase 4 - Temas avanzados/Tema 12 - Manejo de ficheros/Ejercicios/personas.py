from io import open

import sys 
print( sys.getdefaultencoding() )

fichero = open('personas.txt','r')
lineas = fichero.readlines()

personas = []
for linea in lineas:
    campos = linea.replace("\n", "").split(";")  # borramos los saltos de línea y separamos
    persona = {"id":campos[0], "nombre":campos[1], "apellido":campos[2], "nacimiento":campos[3]}
    personas.append(persona)
    
for persona in personas:
    print(persona['apellido'])