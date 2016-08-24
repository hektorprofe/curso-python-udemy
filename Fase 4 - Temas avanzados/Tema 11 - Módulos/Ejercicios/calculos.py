from operaciones import * 

a, b, c, d = (10, 5, 0, "Hola")

print( "{} + {} = {}".format(a, b, suma(a, b) ) )
print( "{} - {} = {}".format(b, d, resta(b, d) ) )
print( "{} * {} = {}".format(b, b, producto(b, b) ) ) 
print( "{} / {} = {}".format(a, c, division(a, c) ) )