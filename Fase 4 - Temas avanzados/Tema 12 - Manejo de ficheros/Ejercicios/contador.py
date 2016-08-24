from io import open
import sys

fichero = open('contador.txt','a+')  # Primero nos aseguramos de abrir el fichero o crearlo
fichero.seek(0)  # Ponemos el puntero al principio
contenido = fichero.readline()  # Leemos la primera línea
if len(contenido) == 0:  # Si está vacío
    contenido = "0"  
    fichero.write(contenido)  # Escribimos el 0 en forma de texto
fichero.close()  # Cerramos el fichero

# Ahora intentamos transformar el texto a un número
try:
    contador = int(contenido)
    
    # Y en función de lo que el usuario quiere...
    if len(sys.argv) == 2:
        if sys.argv[1] == "inc":
            contador += 1
        elif sys.argv[1] == "dec":
            contador -= 1
            
    print(contador)
    
    # Finalmente reabrimos el fichero en modo escritura para reescribir el contador borrando todo
    fichero = open('contador.txt','w')
    fichero.write( str(contador) )
    fichero.close()
    
except:
    print("Ha ocurrido un error, el fichero está corrupto.")