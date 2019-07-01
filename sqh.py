import socket



class Seq_help:
    IP      =   "192.168.1.1"
    PORT    =   5015

    def __init__(self,IP,PORT):
        self.IP = IP
        self.PORT = PORT
        # 接続処理
        client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect((ip,port))



    def reconnect(self):
        # 再接続処理
        return 0

    def Word_read(self):
        return 0
        #D B などの ワード単位リード

    def Bit_read(self):
        # M Y X などの ビット単位リード
        return 0

    def Word_write(self):
        # ワード書き込み
        return 0


    def Bit_write(self):
        # ビット書き込み
        return 0


