import sys
if len(sys.argv) == 3:
	texto = sys.argv[1]
	repeticiones = int(sus.argv[2])
	for r in range(repeticiones):
		print(texto)
else:
	print("Error - Introduce los argumentos correctamente")
	print('Ejemplo: escribir_lineas.py "Texto" 5')