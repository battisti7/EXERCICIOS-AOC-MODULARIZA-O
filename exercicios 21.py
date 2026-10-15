import os

nome: str = ""
nota1: float = 0.0
nota2: float = 0.0
nota3: float = 0.0
nota4: float = 0.0
valor_media: float = 0.0
dir: str = "/tmp/exercicios"
arq: str = "ex21.txt"

def med(n1, n2, n3, n4):
    media: float = (n1 + n2 + n3 + n4) / 4
    return media

def escreveArq(caminho, arquivo, linha_cad):
    file = ""
    tipo = ""
    enc = ""
    
    if not os.path.exists(caminho) or not os.path.isdir(caminho):
        os.makedirs(caminho)
        os.chmod(caminho, 0o744)
        
    caminho_completo = os.path.join(caminho, arquivo)
    
    if os.path.exists(caminho_completo):
        tipo = 'a'
    else:
        tipo = 'w'
        
    with open(caminho_completo, tipo) as file:
        file.write(linha_cad)

def cadastro(nm, nt1, nt2, nt3, nt4, vlr_med):
    global dir, arq
    linha: str = ""
    
    linha = f"{nm};{str(nt1)};{str(nt2)};{str(nt3)};{str(nt4)};{str(vlr_med)}\n"
    
    escreveArq(dir, arq, linha)

def entrada():
    global nome, nota1, nota2, nota3, nota4, valor_media
    
    nome = input("Nome do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    nota4 = float(input("Nota 4: "))
    
    valor_media = med(nota1, nota2, nota3, nota4)
    print(f"Média: {valor_media:.2f}")
    
    cadastro(nome, nota1, nota2, nota3, nota4, valor_media)

def main():
    if not os.path.exists(dir) or not os.path.isdir(dir):
        os.makedirs(dir)
        os.chmod(dir, 0o744)
        
    for contador in range(5):
        entrada()
        
    print(f"Gravado em {os.path.join(dir, arq)}")

if __name__ == "__main__":
    main()