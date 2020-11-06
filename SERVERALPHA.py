
import socket
import threading
import sqlite3
import os.path

ip = "127.0.0.1"
port = 7000
server
    while True:
        s.listen()
        print("\n\tIl server è attivo\n")
        conn, add = s.accept()
        print("\n\tConnessione eseguita\n")
        t = ClietThread(add[0],add[1],conn)
        t.start()

        
        active_thread.append(t)
        connection_table[conn] = add
)
if __name__ == "__main__":
    server()

