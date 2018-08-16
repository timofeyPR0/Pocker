import socket
import poker
sock = socket.socket()
n = int(input('кол-во игроков (целое положительное число меньше 24): '))
m = int(input('начальный банк каждого игрока: '))
rise = int(input('через сколько кругов повышается блайнд?: '))
conn,addr,cash = [0]*n,[0]*n,[m]*n
deck = poker.newDeck()
for i in range(n):
    sock.bind(("localhost", 8080+i))
    sock.listen(10)
    conn[i], addr[i] = sock.accept()
    conn[i].send(bytes('number: '+str(i), encoding = 'utf-8'))
    sock = socket.socket()
#не знаю, что ниже, но без этого не работает
'''if not data:
    print("No data")
    conn.close()'''
cycle = 0
blind = 5
while len(cash)!=1:
    game(cash,blind)
    cycle+=1
    if cycle % rise == 0:
        blind+=5
for i in range(n):
    conn[i].close()
