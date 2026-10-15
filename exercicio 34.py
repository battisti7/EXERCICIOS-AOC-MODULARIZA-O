import os

valor: int = 0
dir: str = "/tmp/exercicios"
arq: str = "ex34.txt"

def mult(vlr, tab):
    res = vlr * tab
    return res

def grava(c, rslt):
    global dir, arq
    file = ""
    tipo = ""
    enc = ""
    linha = ""
    
    linha = str(rslt) + '\n'
    
    if not os.path.exists(dir) or not os.path.isdir(dir):
        os.makedirs(dir)
        os.chmod(dir, 0o744)
        
    caminho_completo = os.path.join(dir, arq)
    
    if os.path.exists(caminho_completo) and c > 0: 
        tipo = 'a'
    else:
        tipo = 'w'
        
    with open(caminho_completo, tipo) as file:
        file.write(linha)

def main():
    global valor
    
    if not os.path.exists(dir):
        os.makedirs(dir)
        os.chmod(dir, 0o744)

    valor = int(input("Digite um valor entre 1 e 10: "))
    
    for contador in range(10):
        result = mult(valor, contador + 1)
        grava(contador, result)
        
    print(f"Gravado em {os.path.join(dir, arq)}")

if __name__ == "__main__":
    main()