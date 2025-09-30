⚙️ Funcionamento:
O programa carrega o arquivo duplo_bal.json, que deve conter:

Estado inicial
Estados finais
Símbolo branco

Lista de transições no formato:

{
  "from": "q0",
  "read": "0",
  "to": "q1",
  "write": "1",
  "dir": "R"
}


Em seguida, lê o arquivo entrada3.txt, onde cada linha representa uma fita de entrada.

Para cada fita:

A máquina executa passo a passo as transições.
Se o cabeçote sair dos limites, a fita é expandida automaticamente.
O resultado da fita final é salvo em saida.txt.

O programa imprime no console:

1 → caso a execução termine em um estado final (aceitação).
0 → caso não alcance estado final (rejeição).

▶️ Como Executar:

Certifique-se de ter o Python 3 instalado.
Coloque os arquivos duplo_bal.json e entrada3.txt na mesma pasta do código.
Execute o programa no terminal:

python simulador.py

📝 Exemplo de Execução
Arquivo entrada3.txt
101
1100

Saída no console
1
0

Arquivo saida.txt
111
1100_

(O caractere _ representa o símbolo branco definido no JSON.)

🔧 Personalização

Edite o arquivo duplo_bal.json para criar sua própria Máquina de Turing.

Modifique entrada3.txt para testar novas fitas de entrada.

O programa se adapta automaticamente à configuração.

📌 Requisitos

Python 3.x

Biblioteca padrão json (já incluída no Python)
