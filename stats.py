def count_caracters(text):
    """
    Cuenta la frecuencia de cada carácter en un texto.
    """
    char_count = {}
    text = text.lower()
    for char in text:
        if char.isalpha():  # Solo contar letras
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

def make_dict_list(char_count):
    """
    Convierte un diccionario de frecuencias en una lista de diccionarios.
    """
    return [{'char': k, 'num': v} for k, v in char_count.items()]

def sort_on(dictionary):
    """
    Función auxiliar para ordenar por la frecuencia de caracteres.
    """
    return dictionary["num"]

def get_num_words(path_to_file):
    """
    Lee un archivo, cuenta las palabras y caracteres, y genera un informe.
    """
    try:
        with open(path_to_file) as f:
            file_contents = f.read()

            # Contar palabras
            words = file_contents.split()
            word_count = len(words)

            # Contar caracteres (solo letras)
            character_count = count_caracters(file_contents)
            character_list = make_dict_list(character_count)
            character_list.sort(reverse=True, key=sort_on)

            # Generar el informe
            print("============ BOOKBOT ============")
            print(f"Analyzing book found at {path_to_file}...")
            print("----------- Word Count ----------")
            print(f"Found {word_count} total words")
            print("--------- Character Count -------")
            for entry in character_list:
                print(f"{entry['char']}: {entry['num']}")
            print("============= END ===============")

    except FileNotFoundError:
        print(f"Error: El archivo '{path_to_file}' no fue encontrado.")
    except Exception as e:
        print(f"Error inesperado: {e}")