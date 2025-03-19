# Práctica final curso Python: Sistema de Gestión de Biblioteca.

# Definimos la clase de este ejercicio.

class Libro:

    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True 
        Libro.biblioteca.append(self)

    def __str__(self):
        estado = "Sí" if self.disponible else "No"
        return f"-Título: {self.titulo} ({self.autor}) -ISBN: {self.isbn} -Disponible: {estado}"
    
    # Lista que representa la biblioteca
    
    biblioteca = [] 
    
    # Este método agrega un nuevo libro a la biblioteca.

    def agregar(self): 
        print("Libro agregado con éxito.")

    # Este método cambia el estado de disponible a False si el libro está disponible.

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"Libro prestado con éxito.")
        else:
            print(f"El libro '{self.titulo}' no se encuentra disponible en este momento.")

    # Este método cambia el estado de disponible a True si estaba prestado.

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"El libro '{self.titulo}' ha sido devuelto correctamente")
        else:
            print(f"El libro '{self.titulo}' ya estaba disponible")
    
    # Este método muestra una lista con todos los libros de la biblioteca y sus datos. 

    @classmethod
    def mostrar(cls):
        if not cls.biblioteca:
            print("No hay libros en la Biblioteca")
        else:
            print("Libros en la Biblioteca")
            for libro in cls.biblioteca:
                print(libro)
                
    # Este método busca un libro en concreto por su ISBN y lo muestra con todos sus datos.

    @classmethod
    def buscar(cls, isbn):
        for libro in cls.biblioteca:
            if libro.isbn == isbn:
                print(f"Libro encontrado:\n{libro}")
                return
        print(f"No se encontró ningún libro con el ISBN {isbn}.")

def menu():
    print("Bienvenido al Sistema de Gestión de Biblioteca")
    while True:
        print("1. Agregar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Mostrar libros")
        print("5. Buscar libro")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            libro = Libro(titulo, autor, isbn)
            libro.agregar() 

        elif opcion == "2":
            isbn = input("Ingresa el ISBN: ")
            libro = next((libro for libro in Libro.biblioteca if libro.isbn == isbn), None)
            if libro:
                libro.prestar()
            else:
                print("Libro no encontrado.")

        elif opcion == "3":
            isbn = input("Ingresa el ISBN: ")
            libro = next((libro for libro in Libro.biblioteca if libro.isbn == isbn), None)
            if libro:
                libro.devolver()
            else:
                print("Libro no encontrado.")

        elif opcion == "4":
            Libro.mostrar() 

        elif opcion == "5":
            isbn = input("Ingresa el ISBN: ")
            Libro.buscar(isbn) 

        elif opcion == "6":
            print("Gracias por su visita. ¡Esperamos verle pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo seleccionando del 1 al 6")

 
if __name__ == "__main__":
    Libro('La sombra del viento', 'Carlos Ruíz Zafón', '0001')
    Libro('La novia gitana', 'Carmen Mola', '0002')
    Libro('De sangre y cenizas', 'Jennifer L. Armentrout', '0003')
    menu()