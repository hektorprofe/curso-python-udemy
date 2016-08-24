import sys

if len(sys.argv) == 2:
	numero = int(sys.argv[1])
	if numero < 0 or numero > 9999:
		print("Error: Numero incorrecto")
		print('Ejemplo: descomposicion.py [0-9999]')
	else:
		cadena = str(numero)  # Transformamos el número de nuevo a cadena
		longitud = len(cadena)  # Guardamos la longitud de la cadena
		for i in range(longitud):  # Iteramos el mismo de veces que caracteres tiene la cadena
			# El objetivo ahora es conseguir los números en unidades, decenas, centenas...
			print( "{:04d}".format( int(cadena[longitud-1-i]) * 10 ** i) )
else:
	print("Error - Argumentos incorrectos")
	print('Ejemplo: descomposicion.py [0-9999]')
