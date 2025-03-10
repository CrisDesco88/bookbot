import sys
from stats import get_num_words
def main():
    # Verificar que se proporcione la ruta del libro como argumento
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Obtener la ruta del libro desde los argumentos de línea de comandos
    path_to_file = sys.argv[1]
    get_num_words(path_to_file)

# Ejecutar la función principal
if __name__ == "__main__":
    main()