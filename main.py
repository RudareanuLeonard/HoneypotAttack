from honeypots.ssh_honeypot import SSHHoneypot

test_ssh_honeypot = SSHHoneypot("127.0.0.1", 2222, "root", "someRandomPassword")



test_ssh_honeypot.connect()


print("Did it!")