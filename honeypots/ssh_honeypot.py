from .basic_honeypot import BasicHoneypot
import paramiko
import socket
import time
class SSHHoneypot(BasicHoneypot):
    def __init__(self, server_ip, port, username, password):
        super().__init__(server_ip, port, username, password)

    def connect(self):

        try:
            #ssh = paramiko.SSHClient()
            #ssh.set_missing_host_key_policy(paramiko.RejectPolicy()) #add unknown keys to hosts keys
            #ssh.load_system_host_keys()
            #ssh.connect(self.server_ip, self.port, self.username, self.password)
            #stdin, stdout, stderr = ssh.exec_command("whoami")

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.server_ip, self.port))
            transport = paramiko.Transport(s)

            transport.connect(username=self.username, password=self.password)
            channel = transport.open_channel("session") #open channel for transporting --- i think i can use open_session too because the "kind" of this channel is session
            
            #only one command then close... i'll use invoke_shell/get_pty for getting multiple commands
            stdin = channel.get_pty("ls -l")
            stdout = channel.get_pty("ls -l")
            stderr = channel.get_pty("ls -l")
            
            time.sleep(0.3)

            print(stdout)


        except Exception as e:
            print("ERROR HERE")
            print(e)
