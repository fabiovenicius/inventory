import os
    
    
lista_equipamentos = []
lista_equipamentos =[]

# [46,4,6,9,10,33,48,49,54,57]

path = "C:\\PSTools"
os.chdir(path)
arquivo = "C:\\Users\\fabio\\Documents\\Desenvolvimento\\Inventario\\result_cmd.txt"

def enabling():
    
    

    with open(arquivo,'w') as f:
        for equipamento in lista_equipamentos:       
            f.write("----Inicio do equipamento 10.25.2.{} ---- \n".format(equipamento))
            remoteadmin = os.system("psexec \\\\10.25.2.{} -u Dseg-rc -p D$eg-rc@14 netsh firewall \
                                     set service remoteadmin enable"
            .format(equipamento))
            if remoteadmin == 0:
                os.system("psexec \\\\10.25.2.{} -u Dseg-rc -p D$eg-rc@14 netsh firewall \
                           set portopening tcp 135 RPCSpice".format(equipamento))
                os.system("psexec \\\\10.25.2.{} -u Dseg-rc -p D$eg-rc@14 netsh firewall \
                           set portopening tcp 445 WMISpice".format(equipamento))
                f.write("Comandos executados com exito no equipamento {}. \n".format(equipamento))
            elif remoteadmin == 53:
                f.write("Make sure that the default admin$ share is enabled on 10.25.2.{}. \n".format(equipamento))
            elif remoteadmin == 1326:
                f.write("Nome de usuário ou senha incorretos para 10.25.2.{}. \n".format(equipamento))
            elif remoteadmin ==50:
                f.write("Não há suporte para ao pedido para o equipamento {}.\n".format(equipamento))
            else:
                f.write(remoteadmin)
            f.write("---- Fim do equipamento 10.25.2.{}----\n".format(equipamento))



if __name__ =="__main__":
    enabling()