import socket
import poker
from threading import Thread
class MyThread(Thread):
    conn = socket
    def sendAll(msg):
        for i in conn:
            if (i!=0):
                i.send(bytes(str(msg), encoding = 'utf-8'))
    def toAnswer(i):
        conn[i].send(bytes("answer123", encoding = "utf-8"))
    def newCycle(players):
        deck = poker.newDeck()
        cardsForPlayers = poker.distr(players,deck)
        for i in range(players):
            print(cardsForPlayers[i][0],cardsForPlayers[i][1])
            conn[i].send(bytes("Ваши карты: "+poker.card(cardsForPlayers[i][0])+" "+poker.card(cardsForPlayers[i][1]), encoding = 'utf-8'))
    def toBet(players, bet):
        conn2 = conn
        prev = 0
        last = -1
        b = False
        while not b:
            for i in range(players):
                if (i==last):
                    b = True
                    break
                conn2[i].send(bytes('Текущая ставка:'+str(bet)+'\nНа сколько вы повышаете ставку?', encoding = 'utf-8'))
                MyThread.toAnswer(i)
                a = int(conn2[i].recv(1024).decode('utf-8'))
                if(a!=0):
                    prev = bet
                    last = i
                    bet += a
                    for ee in conn:
                        if (ee!=conn[i]):
                            ee.send(bytes('Игрок '+str(i+1)+' повысил ставку на '+str(a), encoding = 'utf-8'))

    def main():
        global conn
        sock = socket.socket()
        n = int(input('Количество игроков (целое положительное число меньше 24): '))
        m = int(input('Начальный банк каждого игрока: '))
        rise = int(input('Через сколько кругов повышается блайнд?: '))
        conn,addr,cash  = [0]*n,[0]*n,[m]*n
        blind = 5
        for i in range(n):
            sock.bind(("localhost", 8080+i))
            sock.listen(10)
            conn[i], addr[i] = sock.accept()
            print("(",i+1,") players connected")
            MyThread.sendAll(str(i+1)+"/"+str(n)+" игроков подключено")
            if(i!=n-1):
                conn[i].send(bytes('Вы подключены как игрок номер '+str(i+1)+', ожидаем других игроков...', encoding = 'utf-8'))  
            else:
                conn[i].send(bytes('Вы подключены как игрок номер '+str(i+1)+', вы - последний игрок.', encoding = 'utf-8'))  
            sock = socket.socket()
        MyThread.newCycle(n)
        MyThread.toBet(n,blind)
        '''if(MyThread.b==False):
                msg_thread = MyThread("msg")
                msg_thread.start()
                b = True'''
        #не знаю, что ниже, но без этого не работает
        '''if not data:
            print("No data")
            conn.close()
        cycle = 0
        blind = 5
        while len(cash)!=1:
            game(cash,blind)
            cycle+=1
            if cycle % rise == 0:
                blind+=5'''
        for i in range(n):
            conn[i].close()
    def getAnswer(i):
        while True:
            data = conn[i].recv(1024)
            print("player said: ",data.decode("utf-8"))
            if not data:
                print("end")
                break
    def __init__(self, name):
        """Инициализация потока"""
        Thread.__init__(self)
        self.name = name
    
    def run(self):
        """Запуск потока"""
        if(self.name == "main"):
            MyThread.main()
        elif(self.name == "msg"):
            MyThread.getAnswer(MyThread.conn)
    
if __name__ == "__main__":
    main_thread = MyThread("main")
    main_thread.start()
    
