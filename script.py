def ler_e_escrever():
    """Parte 1: Ler input.txt, transformar em maiúsculas e salvar em output.txt"""
    with open("input.txt", "r", encoding="utf-8") as infile:
        conteudo = infile.read()

    modificado = conteudo.upper()

    with open("output.txt", "w", encoding="utf-8") as outfile:
        outfile.write(modificado)

    print("✅ Arquivo processado! Conteúdo modificado gravado em output.txt")


def leitura_segura():
    """Parte 2: Pedir nome do arquivo e tratar erros"""
    try:
        arquivo = input("Digite o nome do arquivo para leitura: ")
        with open(arquivo, "r", encoding="utf-8") as f:
            conteudo = f.read()
        print("📄 Conteúdo do arquivo:\n", conteudo)

    except FileNotFoundError:
        print("❌ Erro: Arquivo não encontrado.")
    except PermissionError:
        print("❌ Erro: Permissão negada.")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")


if __name__ == "__main__":
    print("=== Parte 1: Ler e escrever ===")
    ler_e_escrever()

    print("\n=== Parte 2: Leitura segura com tratamento de erros ===")
    leitura_segura()
