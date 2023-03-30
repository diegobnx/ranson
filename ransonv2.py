from cryptography.fernet import Fernet
import os

def generate_key(key_path: str):
    # Gerando uma chave simétrica aleatória
    key = Fernet.generate_key()
    with open(key_path, 'wb') as key_file:
        key_file.write(key)

def encrypt_folder(folder_path: str, key: bytes):
    # Criando um objeto Fernet com a chave fornecida
    fernet = Fernet(key)

    # Criptografando todos os arquivos na pasta
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                encrypted_data = fernet.encrypt(file.read())
            with open(file_path, 'wb') as file:
                file.write(encrypted_data)

def decrypt_folder(folder_path: str, key: bytes):
    # Criando um objeto Fernet com a chave fornecida
    fernet = Fernet(key)

    # Descriptografando todos os arquivos na pasta
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                decrypted_data = fernet.decrypt(file.read())
            with open(file_path, 'wb') as file:
                file.write(decrypted_data)

def prompt_folder_selection():
    folder_path = input("Digite o caminho da pasta a ser selecionada: ")
    if not os.path.exists(folder_path):
        print("A pasta informada não existe!")
        exit()
    return folder_path

def prompt_key_selection():
    key_path = input("Digite o caminho do arquivo de chave: ")
    if not os.path.exists(key_path):
        print("O arquivo de chave informado não existe!")
        return None
    with open(key_path, 'rb') as key_file:
        key = key_file.read()
    return key

def encrypt_prompt_folder_selection():
    folder_path = prompt_folder_selection()
    if folder_path:
        key_path = input("Digite o caminho para salvar a chave: ")
        generate_key(key_path)
        with open(key_path, 'rb') as key_file:
            key = key_file.read()
        encrypt_folder(folder_path, key)

def decrypt_prompt_folder_selection():
    folder_path = prompt_folder_selection()
    if folder_path:
        key = prompt_key_selection()
        if key:
            decrypt_folder(folder_path, key)

# Solicitando ao usuário se deseja criptografar ou descriptografar
choice = input("Digite 'E' para criptografar uma pasta ou 'D' para descriptografar uma pasta: ")
if choice == 'E':
    encrypt_prompt_folder_selection()
elif choice == 'D':
    decrypt_prompt_folder_selection()
else:
    print("Escolha inválida. Saindo...")

