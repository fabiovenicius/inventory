import os
arquivo = "ativos.txt"

def funcao():

    rede = input("Informe a rede:")       
    with open(arquivo,'w') as f:
        for host in range(1,255):
            ping_ip = "ping {}.{}".format(rede,host)
            if os.system(ping_ip) == 0:
                computadores = "Computador: {}.{}\n".format(rede, host)
                # print(computadores)
                f.write(computadores)


if __name__ == '__main__':
    funcao()