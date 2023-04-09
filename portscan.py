import sys
import socket

ipEndereco = sys.argv[1]
portas_comuns = [21, 22, 23, 25, 53, 80, 110, 119, 123, 143, 161, 194, 389, 443, 465, 514, 587, 993, 995, 1433, 1521, 3306, 3389, 5432, 8080]


for ports in portas_comuns: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if s.connect_ex((ipEndereco, ports)) == 0:
                
                print(f"Porta {ports} aberta!")
                s.close()
        else:
                print(f"porta {ports} fechada")



