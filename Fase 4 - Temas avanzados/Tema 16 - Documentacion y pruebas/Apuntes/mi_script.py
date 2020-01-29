def suma(a, b):
    """Esta función recibe dos parámetros y devuelve la suma de ambos
    
    >>> suma(5,10)
    15
    """
    return a+b
    
if __name__ == "__main__":   # Cuando se llama al script
    import doctest
    doctest.testmod()
    
print(__name__)