def read_and_modify_file():
    try:
        # Nome fixo do arquivo de entrada
        filename = "input.txt"

        # Abrir e ler o arquivo
        with open(filename, "r", encoding="utf-8") as infile:
            content = infile.read()

        # Contar palavras
        word_count = len(content.split())

        # Converter texto para maiúsculas
        modified_content = content.upper()

        # Nome do arquivo de saída
        new_filename = "output.txt"
        with open(new_filename, "w", encoding="utf-8") as outfile:
            outfile.write("=== PROCESSED TEXT ===\n")
            outfile.write(modified_content + "\n\n")
            outfile.write(f"Word count: {word_count}\n")

        print(f"✅ File processed successfully! Output saved as '{new_filename}'.")

    except FileNotFoundError:
        print("❌ Error: input.txt not found.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


# Executar função principal
if __name__ == "__main__":
    read_and_modify_file()
