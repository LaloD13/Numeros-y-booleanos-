#Strings
"""Juan Eduardo Doria Villanueva 
2630021 IM_3"""
"""
Un string en Python es un tipo de dato (str) que almacena una secuencia de caracteres de texto
y se caracteriza por ser inmutable, es decir, no puede modificarse una vez que ha sido creado.
Entre las operaciones básicas que permite están: concatenar (+), obtener su longitud (len()),
extraer sub-cadenas mediante slicing, buscar patrones (find) y reemplazar texto (replace).
Es vital validar y normalizar el texto de entrada (como correos, nombres o contraseñas) para
prevenir vulnerabilidades de seguridad, errores en procesos y garantizar datos consistentes.
Este documento cubrirá: la descripción detallada de cada problema, el diseño de entradas y salidas,
las validaciones aplicadas y el uso de métodos de string junto con sus casos de prueba y código.
"""

#Buenas Practicas
"""Incluye una pequeña sección en comentarios donde menciones:
- Los strings son inmutables: cualquier cambio genera una nueva cadena.
- Es buena práctica normalizar entrada con strip() y lower() antes de compararla.
- Evitar "números mágicos" en índices; documentar qué extrae cada slice.
- Usar métodos de string en lugar de reescribir lógica básica.
- Diseñar validaciones claras: primero que no esté vacío, luego el formato.
- Escribir código legible: nombres de variables claros y mensajes de error entendibles.
"""

print("\n Problem 1: full name formatter (name + initials)".upper())
"""Descripcion: dado el nombre completo de una persona en una sola cadena el programa debe de:
Normalizar el texto(strip, espacios extra, mayusculas/minisculas)
Mostrar el nombre formateado en Title Case y las iniciales"""

# Inputs:
# - full_name (string)
#
# Outputs:
# - "Formatted name: <Name In Title Case>"
# - "Initials: <X.X.X.>"
#
# Validations:
# - full_name no vacío tras strip().
# - Debe contener al menos dos palabras.
full_name = "   juan eduardo doria   "

clean_name = full_name.strip()

if clean_name == "":
    print("Error: El nombre no puede estar vacío.")
else:
    words = clean_name.split()
    
    if len(words) < 2:
        print("Error: El nombre debe contener al menos dos palabras.")
    else:
        formatted_name = ""
        initials = ""
        
        for word in words:
            formatted_name = formatted_name + word.title() + " "
            initials = initials + word[0].upper() + "."
            
        print("Formatted name: " + formatted_name.strip())
        print("Initials: " + initials)

print("\nPROBLEM 2: Simple email validator (structure + domain)".upper())
"""descripcion: valida si una direccion de correo tiene un formato basico correcto"
-contiene exactamente un "@"
-despues del "@" debe haber al menos un ".".
-no tener espacios en blanco 
si el correo es valida,tambien muestra el dominio 
"""

# Inputs:
# - email_text (string)
#
# Outputs:
# - "Valid email: true" o "Valid email: false"
# - "Domain: <domain_part>"
#
# Validations:
# - email_text no vacío tras strip().
# - Contiene exactamente un '@'.
# - No contiene espacios en blanco.
# - Al menos un '.' después del '@'.
    
email_text = "2630021@upv.com"

email = email_text.strip()

if email == "":
    print("Valid email: false")
elif " " in email:
    print("Valid email: false")
else:
    arrobas = 0
    for char in email:
        if char == "@":
            arrobas = arrobas + 1
            
    if arrobas != 1:
        print("Valid email: false")
    else:
        at_index = email.find("@")
        domain = email[at_index + 1:]
        
        tiene_punto = False
        for char in domain:
            if char == ".":
                tiene_punto = True
                
        if tiene_punto == False:
            print("Valid email: false")
        else:
            print("Valid email: true")
            print("Domain: " + domain)

print("\nProblem 3: Palindrome checker".upper())
"""
Descripción:
Determina si una frase es un palíndromo, 
es decir, se lee igual de izquierda a derecha y de derecha a izquierda,
ignorando espacios y mayúsculas/minúsculas.
"""
# Inputs:
# - phrase (string)
#
# Outputs:
# - "Is palindrome: true/false"
# - "Normalized: <phrase>"
#
# Validations:
# - phrase no vacía tras strip().
# - Al menos 3 caracteres tras normalizar.

phrase = "Anita lava la tina"

clean_phrase = phrase.strip()

if clean_phrase == "":
    print("Error: La frase no puede estar vacía.")
else:
    normalized_phrase = ""
    for char in clean_phrase:
        if char != " ":
            normalized_phrase = normalized_phrase + char.lower()
            
    if len(normalized_phrase) < 3:
        print("Error: La frase debe tener al menos 3 letras.")
    else:
        reversed_phrase = ""
        for char in normalized_phrase:
            reversed_phrase = char + reversed_phrase 
            
        if normalized_phrase == reversed_phrase:
            print("Is palindrome: true")
        else:
            print("Is palindrome: false")
            
        print("Normalized: " + normalized_phrase)

print("\nProblem 4: Sentence word stats (lengths and first/last word)".upper())
"""descripcion: Descripción:
Dada una oración, el programa debe:
1) Normalizar espacios (quitar espacios al principio y al final).
2) Separar las palabras por espacios.
3) Mostrar:
   - Número total de palabras.
   - Primera palabra.
   - Última palabra.
   - Palabra más corta y más larga (por longitud)."""

# Inputs:
# - sentence (string)
#
# Outputs:
# - "Word count: <n>"
# - "First word: <...>", "Last word: <...>"
# - "Shortest word: <...>", "Longest word: <...>"
#
# Validations:
# - Oración no vacía tras strip().
# - Debe contener al menos una palabra.
sentence = "El veloz murcielago hindu comia feliz cardillo y kiwi"

clean_sentence = sentence.strip()

if clean_sentence == "":
    print("Error: La oración no puede estar vacía.")
else:
    words = clean_sentence.split()
    
    if len(words) >= 1:
        word_count = len(words)
        first_word = words[0]
        last_word = words[-1]
        
        shortest_word = words[0]
        longest_word = words[0]
        
        for word in words:
            if len(word) < len(shortest_word):
                shortest_word = word
            if len(word) > len(longest_word):
                longest_word = word
                
        print("Word count: " + str(word_count))
        print("First word: " + first_word)
        print("Last word: " + last_word)
        print("Shortest word: " + shortest_word)
        print("Longest word: " + longest_word)

print("\nProblem 5: Password strength classifier".upper())
"""
Descripción:
Clasifica una contraseña como "weak", "medium" o "strong" según reglas mínimas
(puedes afinarlas, pero documéntalas en los comentarios)
"""
# Inputs:
# - password_input (string)
#
# Outputs:
# - "Password strength: weak | medium | strong"
#
# Validations:
# - Contraseña no vacía.

print("\nPROBLEM 5")
password_input = "HolaMundo123!"

if password_input == "":
    print("Error: La contraseña no puede estar vacía.")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    for char in password_input:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char.isalnum() == False:
            has_special = True
            
    if len(password_input) >= 8 and has_upper and has_lower and has_digit and has_special:
        print("Password strength: strong")
    elif len(password_input) < 8 or (has_lower and not has_upper and not has_digit and not has_special):
        print("Password strength: weak")
    else:
        print("Password strength: medium")

print("\nProblem 6: Product label formatter (fixed-width text".upper())

"""
Descripción:
Dado el nombre de un producto y su precio, genera una etiqueta en una sola línea con el siguiente formato
Product: <NAME> | Price: $<PRICE>

La cadena completa debe tener exactamente 30 caracteres:
- Si es más corta, rellena con espacios al final.
- Si es más larga, recorta hasta 30 caractere
"""

#
# Inputs:
# - product_name (string)
# - price_value (string o número)
#
# Outputs:
# - "Label: <exactly 30 characters>"
#
# Validations:
# - product_name no vacío tras strip().
# - price_value debe ser un número positivo.

product_name = "Televisor Ultra HD 4K 55 pulgadas"
price_value = 450

clean_name = product_name.strip()

if clean_name == "":
    print("Error: El nombre no puede estar vacío.")
elif float(price_value) < 0:
    print("Error: El precio debe ser positivo.")
else:
    price_str = str(price_value)
    
    letras_fijas = 10 + len(price_str)
    espacio_para_nombre = 30 - letras_fijas
    
    nombre_final = ""
    
    if len(clean_name) > espacio_para_nombre:
        contador = 0
        for char in clean_name:
            if contador < espacio_para_nombre:
                nombre_final = nombre_final + char
                contador = contador + 1
    else:
        nombre_final = clean_name
        
    base_label = "Product: " + nombre_final + " | Price: $" + price_str
    
    espacios_faltantes = 30 - len(base_label)
    final_label = base_label
    
    for i in range(espacios_faltantes):
        final_label = final_label + " "
        
    print("Label: '" + final_label + "'")
"""
Python Software Foundation. (2024). Built-in Types: Text Sequence Type — str. Python 3.12 Documentation. Recuperado de la documentación oficial. (Referencia para métodos de limpieza y partición como .strip(), .split() y .join()).

Python Software Foundation. (2024). Built-in Types: String Methods. Python 3.12 Documentation. (Referencia para validaciones de caracteres como .isalnum(), .isdigit(), .isupper() y .islower()).

Real Python. (2023). Python String Formatting Best Practices. Real Python Tutorials. (Referencia que sustenta el uso de f-strings f"..." para la interpolación eficiente de variables en textos).

Python Software Foundation. (2024). Built-in Functions: len(). Python 3.12 Documentation. (Referencia técnica sobre el funcionamiento del conteo de elementos en estructuras de datos iterables).

Sweigart, A. (2019). Automate the Boring Stuff with Python (2da ed.). No Starch Press. (Capítulo 6: Manipulación de Strings, aplicable a los algoritmos de extracción de dominio y análisis de palíndromos).

"""