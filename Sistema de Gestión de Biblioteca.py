# Práctica final curso Python: Sistema de Gestión de Biblioteca.
class Libro:

    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True 
        
    def __str__(self):
        estado = "Sí" if self.disponible else "No"
        return f"-Título: {self.titulo} ({self.autor}) -ISBN: {self.isbn} -Disponible: {estado}"

    # Cambia el estado de disponible a False si el libro está disponible.
    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"Libro prestado con éxito.")
        else:
            print(f"El libro '{self.titulo}' no se encuentra disponible en este momento.")

    # Cambia el estado de disponible a True si estaba prestado.
    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"El libro '{self.titulo}' ha sido devuelto correctamente")
        else:
            print(f"El libro '{self.titulo}' ya estaba disponible")
 
class Biblioteca:

    def __init__(self, libros):
        self.libros = libros

    # Agrega un nuevo libro a la biblioteca.
    def agregar(self, libro): 
        self.libros.append(libro)
        print("Libro agregado con éxito.")

    # Muestra una lista con todos los libros de la biblioteca y sus datos. 
    def mostrar(self):
        if not self.libros:
            print("No hay libros en la Biblioteca")
        else:
            print("Libros en la Biblioteca")
            for libro in self.libros:
                print(libro)
                
    # Busca un libro en concreto por su ISBN y lo muestra con todos sus datos.
    def buscar(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                print(f"Libro encontrado:\n{libro}")
                return
        print(f"No se encontró ningún libro con el ISBN {isbn}.")

def main():

    biblioteca = Biblioteca(
        [Libro('La sombra del viento', 'Carlos Ruíz Zafón', '0001'),
         Libro('La novia gitana', 'Carmen Mola', '0002'),
         Libro('De sangre y cenizas', 'Jennifer L. Armentrout', '0003')])

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
            biblioteca.agregar(libro)

        elif opcion == "2":
            isbn = input("Ingresa el ISBN: ")
            libro = next((libro for libro in biblioteca.libros if libro.isbn == isbn), None)
            if libro:
                libro.prestar()
            else:
                print("Libro no encontrado.")

        elif opcion == "3":
            isbn = input("Ingresa el ISBN: ")
            libro = next((libro for libro in biblioteca.libros if libro.isbn == isbn), None)
            if libro:
                libro.devolver()
            else:
                print("Libro no encontrado.")

        elif opcion == "4":
            biblioteca.mostrar() 

        elif opcion == "5":
            isbn = input("Ingresa el ISBN: ")
            biblioteca.buscar(isbn) 

        elif opcion == "6":
            print("Gracias por su visita. ¡Esperamos verle pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo seleccionando del 1 al 6")

 
if __name__ == "__main__":
    main()

