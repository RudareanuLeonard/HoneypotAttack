from .basic_honeypot import BasicHoneypot
import paramiko
import socket
import time
from . import interactive #this is a file from paramiko library github/doc



class SSHHoneypot(BasicHoneypot):
    def __init__(self, server_ip, port, username, password):
        super().__init__(server_ip, port, username, password)

    def connect(self):
        try:
            ssh = paramiko.SSHClient()
            #ssh.load_host_keys()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            print("Connecting... ")
            ssh.connect(hostname=self.server_ip, port=self.port, username=self.username, password=self.password)

            channel = ssh.invoke_shell()
            #print("Transport = " + repr(ssh.get_transport()))

            print("Starting shell")
            
            interactive.interactive_shell(channel)
            
            channel.close()
            ssh.close()
            
        except Exception as e:
            print("Error = " + str(e))
