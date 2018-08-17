import socket
import poker
from threading import Thread
class MyThread(Thread):
    conn = socket.socket()
    def main():
        conn = MyThread.conn
        i = 0
        d = 0
        while not d:
            try:
                conn.connect(("127.0.0.1", 8080+i))
                d = conn.recv(1024)
            except:
                i+=1
        print(d.decode("utf-8"))
        answ_thread = MyThread("getansw")
        answ_thread.start()
        
        
        #не знаю, что ниже, но без этого не работает
        '''data = b""
        tmp = conn.recv(1024)
        while tmp:
            data += tmp
            tmp = conn.recv(1024)
        print(data.decode("utf-8"))'''
    def getAnswer():
    #    msg_thread = MyThread("msg")
    #    msg_thread.start()
        while True:
            data = MyThread.conn.recv(1024).decode("utf-8")
            if(data[-9:] == "answer123"):
                print(data[:-9])
                MyThread.conn.send(bytes(input(),encoding = 'utf-8'))
            else:    
                print(">>",data)
            if not data:
                print("end")
                MyThread.conn.close()
                break
    #def answer():
    #    s = input()
    #    while (s!="/exit"):
    #        MyThread.conn.send(bytes(s,encoding = 'utf-8'))
        #MyThread.conn.close()
    def __init__(self, name):
        """Инициализация потока"""
        Thread.__init__(self)
        self.name = name
    
    def run(self):
        """Запуск потока"""
        if(self.name == "main"):
            MyThread.main()
        if(self.name == "msg"):
            MyThread.answer()
        if(self.name == "getansw"):
            MyThread.getAnswer()  
        #msg = "%s is running" % self.name
        #print(msg)
    
if __name__ == "__main__":
    main_thread = MyThread("main")
    main_thread.start()
    
