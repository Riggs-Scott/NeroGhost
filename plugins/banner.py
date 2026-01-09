from colorama import Fore, Back, Style, init
from PIL import Image, ImageDraw, ImageFont
import shutil
import textwrap

init(autoreset=True)

# Centraliza texto no terminal
def centralizar(texto):
    largura = shutil.get_terminal_size().columns
    return texto.center(largura)

# Banner ASCII inicial NeroGhost
def banner_inicial():
    largura = shutil.get_terminal_size().columns
    print("\n" + Back.BLUE + Fore.WHITE + "=" * largura)
    print(Back.BLUE + Fore.YELLOW + centralizar("💥 NEROGHOST 💥"))
    print(Back.BLUE + Fore.WHITE + "=" * largura + "\n")

# Banner ASCII custom
def criar_banner():
    cores_texto = {
        "branco": Fore.WHITE, "amarelo": Fore.YELLOW, "vermelho": Fore.RED,
        "verde": Fore.GREEN, "azul": Fore.BLUE, "magenta": Fore.MAGENTA,
        "ciano": Fore.CYAN, "preto": Fore.BLACK
    }
    cores_fundo = {
        "branco": Back.WHITE, "amarelo": Back.YELLOW, "vermelho": Back.RED,
        "verde": Back.GREEN, "azul": Back.BLUE, "magenta": Back.MAGENTA,
        "ciano": Back.CYAN, "preto": Back.BLACK
    }

    while True:
        titulo = input("Digite o título do banner: ")
        cor_fundo = input("Escolha a cor de fundo: ").lower()
        cor_texto = input("Escolha a cor do texto: ").lower()
        emojis = input("Emojis (Enter para nenhum): ")
        conteudo = f"{emojis} {titulo} {emojis}" if emojis else titulo

        fundo = cores_fundo.get(cor_fundo, Back.BLACK)
        texto = cores_texto.get(cor_texto, Fore.WHITE)
        largura = shutil.get_terminal_size().columns
        linha = fundo + texto + "=" * largura

        print("\n" + linha)
        print(fundo + texto + centralizar(conteudo))
        print(linha + "\n")

        salvar = input("Salvar em .txt? (s/n): ").lower()
        if salvar == "s":
            nome_arquivo = titulo.replace(" ", "_") + ".txt"
            with open(nome_arquivo, "w", encoding="utf-8") as f:
                f.write("=" * largura + "\n")
                f.write(centralizar(conteudo) + "\n")
                f.write("=" * largura + "\n")
            print(f"Banner salvo como {nome_arquivo}\n")

        outro = input("Criar outro banner? (s/n): ").lower()
        if outro != "s":
            break

# Função para criar gradiente horizontal
def criar_gradiente(largura, altura, cor_inicio, cor_fim):
    base = Image.new("RGB", (largura, altura), cor_inicio)
    grad = Image.new("RGB", (largura, altura), cor_inicio)
    draw = ImageDraw.Draw(grad)
    for i in range(largura):
        r = int(cor_inicio[0] + (cor_fim[0]-cor_inicio[0]) * i / largura)
        g = int(cor_inicio[1] + (cor_fim[1]-cor_inicio[1]) * i / largura)
        b = int(cor_inicio[2] + (cor_fim[2]-cor_inicio[2]) * i / largura)
        draw.line([(i,0),(i,altura)], fill=(r,g,b))
    return grad

# Banner PRO automático com NeroGhost
def criar_banner_pro():
    while True:
        print("\n🎨 Criando Banner NeroGhost PRO 🎨\n")
        subtitulo = input("Subtítulo (Enter para nenhum): ")
        emojis = input("Emojis (Enter para nenhum): ")
        largura = int(input("Largura do banner (ex: 800): "))
        altura = int(input("Altura do banner (ex: 300): "))
        cor_fundo_inicio = input("Cor inicial do gradiente: ").lower()
        cor_fundo_fim = input("Cor final do gradiente: ").lower()
        cor_texto = input("Cor do texto: ").lower()

        titulo = "NeroGhost"
        conteudo = f"{emojis} {titulo} {emojis}" if emojis else titulo

        img = criar_gradiente(largura, altura, 
                              cores_rgb.get(cor_fundo_inicio,(0,0,0)),
                              cores_rgb.get(cor_fundo_fim,(0,0,0)))
        draw = ImageDraw.Draw(img)

        try:
            font_titulo = ImageFont.truetype("arial.ttf", int(altura/4))
            font_sub = ImageFont.truetype("arial.ttf", int(altura/8))
        except:
            font_titulo = ImageFont.load_default()
            font_sub = ImageFont.load_default()

        w, h = draw.textsize(conteudo, font=font_titulo)
        x = (largura - w)/2
        y = (altura - h)/2 - 20
        draw.text((x,y), conteudo, font=font_titulo, fill=cores_rgb.get(cor_texto,(255,255,255)))

        if subtitulo:
            sub_wrapped = textwrap.fill(subtitulo, width=30)
            w2, h2 = draw.textsize(sub_wrapped, font=font_sub)
            x2 = (largura - w2)/2
            y2 = y + h + 10
            draw.text((x2,y2), sub_wrapped, font=font_sub, fill=cores_rgb.get(cor_texto,(255,255,255)))

        nome_img = f"NeroGhost.png"
        img.save(nome_img)
        print(f"\n✅ Banner salvo como {nome_img}\n")

        outro = input("Criar outro banner? (s/n): ").lower()
        if outro != "s":
            break

# Cores RGB usadas no PRO
cores_rgb = {
    "branco": (255,255,255), "amarelo": (255,255,0), "vermelho": (255,0,0),
    "verde": (0,255,0), "azul": (0,0,255), "magenta": (255,0,255),
    "ciano": (0,255,255), "preto": (0,0,0)
        }
