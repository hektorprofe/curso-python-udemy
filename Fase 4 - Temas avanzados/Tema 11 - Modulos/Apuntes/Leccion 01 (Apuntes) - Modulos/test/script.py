import sys

# for v in sys.path[:]:
#     if v == '..':
#         sys.path.remove(v)

if not ('..' in sys.path):
    sys.path.append('..')
    
print(sys.path)

from saludos import *
Saludo()