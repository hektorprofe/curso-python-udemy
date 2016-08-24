import sys

if len(sys.argv) == 3:
	filas = int(sys.argv[1])
	columnas = int(sys.argv[2])
	if filas < 1 or filas > 10 or columnas < 1 or columnas > 10:
		print("Error: Filas o columnas incorrectas")
		print('Ejemplo: tabla.py [1-10] [1-10]')
	else:
		for f in range(filas):
			print("")  # Salto de línea normal
			for c in range(columnas):
				print(" * ", end='')
else:
	print("Error - Argumentos incorrectos")
	print('Ejemplo: tabla.py [1-10] [1-10]')
