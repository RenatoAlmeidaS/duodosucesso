import socket
import os
import sys


def ler_porta():

    porta = 0
    escolha = 0

    while (escolha < 1 or escolha > 2): 
        os.system("clear")  
        escolha = input("Porta servidor:\n1-Padrao\n2-Digitar porta\n")

    if (escolha == 1):
        porta = 5555
    else:
        porta = input("Digite a porta:\n")

    return porta


HOST = ''              # Endereco IP do Servidor
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
erro_porta = True

while erro_porta:
    try:
        orig = (HOST, ler_porta())
        tcp.bind(orig)
        erro_porta = False
        os.system("clear")
    except Exception as e:
        raw_input("Porta invalida, pressione qualquer tecla para tentar novamente\n")

tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    pid = os.fork()
    if pid == 0:
        tcp.close()
        print'Conectado por', cliente
        while True:
            msg = con.recv(1024)
            print cliente, msg
        print'Finalizando conexao do cliente', cliente
        con.close()
        sys.exit(0)
    else:
        con.close()