from io import open
import pickle

class Personaje:
    
    # Constructor de clase
    def __init__(self, nombre, vida, ataque, defensa, alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance
        # print("Se ha creado el personaje: {}".format(self.nombre) )
        
    def __str__(self):
        return "{} => {} vida, {} ataque, {} defensa, {} alcance".format(self.nombre, self.vida, self.ataque, self.defensa, self.alcance)


class Gestor:
    
    personajes = []
    
    # Constructor de clase
    def __init__(self):
        self.cargar()
        
    def agregar(self, p):
        for pTemp in self.personajes:
            if pTemp.nombre == p.nombre:
                # print("El personaje ya existe en el Gestor.")
                return
        self.personajes.append(p)
        self.guardar()    

    def borrar(self, nombre):
        for i, pTemp in enumerate(self.personajes):
            if pTemp.nombre == nombre:
                print("\nBorrando el personaje", nombre)
                self.personajes.pop(i)
                self.guardar()
                return
        
    def mostrar(self):
        if len(self.personajes) == 0:
            print("\nEl gestor está vacío")
            return
        print("\nMostrando el gestor")
        for p in self.personajes:
            print(p)
            
    def cargar(self):
        fichero = open('personajes.pckl', 'ab+')
        fichero.seek(0)
        try:
            self.personajes = pickle.load(fichero)
        except:
            print("El fichero está vacío")
        finally:
            fichero.close()
            print("Se han cargado {} personajes".format( len(self.personajes)))
    
    def guardar(self):
        fichero = open('personajes.pckl', 'wb')
        pickle.dump(self.personajes, fichero)
        fichero.close()


g = Gestor()
g.mostrar()
g.agregar( Personaje("Caballero",4,2,4,2) )
g.agregar( Personaje("Guerrero",2,4,2,4) )
g.agregar( Personaje("Arquero",2,4,1,8) )
g.mostrar()
g.borrar("Arquero")
g.mostrar()