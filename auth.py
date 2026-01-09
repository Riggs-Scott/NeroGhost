import json
import hashlib
import os

# Cria arquivo se não existir
if not os.path.exists("users.json"):
    with open("users.json", "w") as f:
        json.dump({"usuarios": []}, f, indent=4)

def cadastrar_usuario(username, senha):
    with open("users.json", "r+") as f:
        data = json.load(f)
        for u in data["usuarios"]:
            if u["username"] == username:
                print("Usuário já existe!")
                return False
        hashed = hashlib.sha256(senha.encode()).hexdigest()
        data["usuarios"].append({"username": username, "senha": hashed})
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
        print("Usuário cadastrado com sucesso!")
        return True

def login_usuario(username, senha):
    with open("users.json", "r") as f:
        data = json.load(f)
        hashed = hashlib.sha256(senha.encode()).hexdigest()
        for u in data["usuarios"]:
            if u["username"] == username and u["senha"] == hashed:
                return True
        return False
