from cx_Freeze import setup, Executable
from colorama import Fore, init
init()
print(Fore.MAGENTA + r"""

▀█████████▄  ███    █▄   ▄█   ▄█       ████████▄     ▄████████    ▄████████ 
  ███    ███ ███    ███ ███  ███       ███   ▀███   ███    ███   ███    ███ 
  ███    ███ ███    ███ ███▌ ███       ███    ███   ███    █▀    ███    ███ 
 ▄███▄▄▄██▀  ███    ███ ███▌ ███       ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
▀▀███▀▀▀██▄  ███    ███ ███▌ ███       ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
  ███    ██▄ ███    ███ ███  ███       ███    ███   ███    █▄  ▀███████████ 
  ███    ███ ███    ███ ███  ███▌    ▄ ███   ▄███   ███    ███   ███    ███ 
▄█████████▀  ████████▀  █▀   █████▄▄██ ████████▀    ██████████   ███    ███ 
                             ▀                                   ███    ███ 

""")




input("Welcome To Client-exe builder, Press any key to continue...")
print()
Exe = input("[*] Enter path to Decode-exec-obfusqued python file : ")
base = "Win32GUI" #set None if you want a console

executables = [Executable(Exe, base=base)]

options = {
    'build_exe': {
        'include_files': [],  # Aucun fichier supplémentaire à inclure
        'packages': [],       # Liste des packages à inclure
        'excludes': [],       # Liste des modules à exclure
        'include_msvcr': True,  # Inclure les bibliothèques CRT nécessaires
        'optimize' : True
    }
}

setup(
    name="Client-tool",
    version="2.0",
    description="v2.0-of-Client-pc-helper",
    options=options,
    executables=executables
)

input("Exe-file have been created in the Builder.bat cwd, Press any key...")