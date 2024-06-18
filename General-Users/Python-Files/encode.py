import base64

filePY = input('[*] File to encode : ')

# Ouvrir le fichier et lire son contenu
with open(filePY, 'r') as original_script:
    code = original_script.read()

# Diviser le script en deux moitiés si nécessaire
# Exemple de division en deux moitiés (pour l'illustration, vous pouvez ajuster selon vos besoins)
# code_partie1 = code[:len(code)//2]
# code_partie2 = code[len(code)//2:]

# Encoder le code en Base64
encoded_code = base64.b64encode(code.encode()).decode()

# Imprimer les parties encodées pour les copier dans le script de décodage
print(f"Encoded code (Base64): {encoded_code}")
print()

input("Press Any key To End")