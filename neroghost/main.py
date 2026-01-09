from auth import cadastrar_usuario, login_usuario
from banner import criar_banner, banner_inicial, criar_banner_pro

def dashboard(username):
    while True:
        banner_inicial()
        print(f"Bem-vindo, {username}!\n")
        print("1️⃣ Criar Banner ASCII (terminal)")
        print("2️⃣ Criar Banner NeroGhost PRO (.png automático)")
        print("3️⃣ Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            criar_banner()
        elif escolha == "2":
            criar_banner_pro()
        elif escolha == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.\n")

def iniciar():
    print("🎮 Bem-vindo ao painel NeroGhost 🎮\n")
    while True:
        print("1️⃣ Login")
        print("2️⃣ Cadastrar")
        print("3️⃣ Sair")
        op = input("Escolha: ")

        if op == "1":
            user = input("Usuário: ")
            senha = input("Senha: ")
            if login_usuario(user, senha):
                dashboard(user)
            else:
                print("❌ Login incorreto!\n")
        elif op == "2":
            user = input("Novo usuário: ")
            senha = input("Senha: ")
            cadastrar_usuario(user, senha)
        elif op == "3":
            print("Saindo do painel...")
            break
        else:
            print("Opção inválida, tente novamente.\n")

if __name__ == "__main__":
    iniciar()
