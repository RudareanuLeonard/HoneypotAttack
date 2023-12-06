from honeypots.ssh_honeypot import SSHHoneypot
from boofuzz import *

class Fuzzing(SSHHoneypot):
    def __init__(self, server_ip, port, username, password):
        super().__init__(server_ip, port, username, password)

    def fuzzing(self):
        session = Session(
            target=Target(connection=TCPSocketConnection(self.server_ip, int(self.port)))
        )

        s_initialize("FUZZ AGAINST COWRIE")
        s_string("FUZZING")
        s_static("\r\n")

        session.connect(s_get("FUZZ AGAINST COWRIE"))

        session.fuzz()
