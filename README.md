# Relógio de Lamport

Implementação que simula o relógio de Lamport, na comunicação entre 1 servidor e 2 clientes diferentes. 

## Pré-requisitos
Python3

## Uso
Coloquei um IP e porta da instância servidor da AWS previamente configuradas no grupo de segurança. Para testar com outra máquina, deve-se substituir.
O teste que fiz no vídeo foi executar o servidor primeiro, depois um cliente em outra instância. Antes que terminasse a execução deste, executar também o segundo cliente, a fim do servidor atender aos dois de forma concorrente.

1. Executar o servidor
```bash
   python3 server.py porta
```

2. Executar o 1º cliente
```bash
   python3 client1.py ip_publico porta
```
3. Executar o 2º cliente
```bash
   python3 client2.py ip_publico porta
```
Depois desses processos, obtive a seguinte saída:

Servidor:
```bash
   Server started!
   Waiting for clients...
   Message received from ('52.23.209.141', 39320) at  (LAMPORT_TIME=4)
   Message received from ('52.201.232.21', 49628) at  (LAMPORT_TIME=5)
   Message sent to ('52.23.209.141', 39320) at  (LAMPORT_TIME=6)
   Message received from ('52.23.209.141', 39320) at  (LAMPORT_TIME=9)
   Message sent to ('52.201.232.21', 49628) at  (LAMPORT_TIME=10)
   Message sent to ('52.23.209.141', 39320) at  (LAMPORT_TIME=11)
```

Cliente 1:
```bash
   This IP address is:  52.23.209.141
   Something happened here... at  (LAMPORT_TIME=1)
   Connection Request at  (LAMPORT_TIME=2)
   Message sent to 54.167.168.142 at  (LAMPORT_TIME=3)
   Message received from 54.167.168.142 at  (LAMPORT_TIME=7)
   Message sent to 54.167.168.142 at  (LAMPORT_TIME=8)
   Message received from 54.167.168.142 at  (LAMPORT_TIME=12)
```

Cliente 2:
```bash
   This IP address is:  52.201.232.21
   Connection Request at  (LAMPORT_TIME=1)
   Message sent to 54.167.168.142 at  (LAMPORT_TIME=2)
   Message received from 54.167.168.142 at  (LAMPORT_TIME=11)
```
