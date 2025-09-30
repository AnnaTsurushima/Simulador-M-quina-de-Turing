import json

def main():
    # Caminho do arquivo JSON (configuração da máquina de Turing)
    caminho_json = r"C:\Códigos vscodes\Teoria da Computação\Maquina de Turing Universal\duplo_bal.json"
    
    # Tentativa de carregar o arquivo JSON
    try:
        with open(caminho_json, 'r') as f_json:
            maquina = json.load(f_json)
    except FileNotFoundError:
        print("Erro: Arquivo JSON não encontrado.")
        return

    # Caminho do arquivo de entrada
    caminho_entrada = r"C:\Códigos vscodes\Teoria da Computação\Maquina de Turing Universal\entrada3.txt"
    
    # Tentativa de abrir arquivo de entrada
    try:
        with open(caminho_entrada, 'r') as f_txt:
            entradas = f_txt.readlines()
    except FileNotFoundError:
        print("Erro: Arquivo de entrada TXT não encontrado.")
        return
    
    # Informações da máquina
    transicoes = maquina['transitions']
    transicoes_dict = {(t['from'], t['read']): t for t in transicoes}  # Busca rápida
    simbolo_branco = maquina['white']
    estados_finais = maquina['final']
    estado_inicial = maquina['initial']
    
    # Arquivo de saída
    with open("saida.txt", "w") as f_saida:
        # Processa cada palavra de entrada
        for palavra in entradas:
            fita = list(palavra.strip())  # Converte string em lista mutável
            estado = estado_inicial
            cabecote = 0
            
            # Loop da execução da máquina
            while estado not in estados_finais:
                simbolo_atual = fita[cabecote]
                chave = (estado, simbolo_atual)
                
                # Verifica se existe transição
                if chave in transicoes_dict:
                    regra = transicoes_dict[chave]
                    
                    # Atualiza fita e estado
                    fita[cabecote] = regra['write']
                    estado = regra['to']
                    
                    # Move o cabeçote
                    if regra['dir'] == 'R':
                        cabecote += 1
                    elif regra['dir'] == 'L':
                        cabecote -= 1
                else:
                    break  # Sem transição → parar execução
                
                # Expansão da fita (quando cabeçote ultrapassa limites)
                if cabecote < 0:
                    fita.insert(0, simbolo_branco)
                    cabecote = 0
                elif cabecote >= len(fita):
                    fita.append(simbolo_branco)
            
            # Salva resultado da fita
            f_saida.write(''.join(fita) + '\n')
            
            # Imprime aceitação (1) ou rejeição (0)
            print(1 if estado in estados_finais else 0)


if __name__ == "__main__":
    main()
