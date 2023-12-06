from honeypots.ssh_honeypot import SSHHoneypot
from attacks.fuzzing import Fuzzing
from attacks.dos import DoS
import time
import threading

test_ssh_honeypot = SSHHoneypot("127.0.0.1", "2222", "root", "someRandomPassword")

test_ssh_honeypot.connect()

# test_fuzzing = Fuzzing(test_ssh_honeypot.server_ip, test_ssh_honeypot.port, test_ssh_honeypot.username, test_ssh_honeypot.password)
# test_fuzzing.fuzzing()


print("Prepare for DoS attack...")
time.sleep(3)
print()
print()

test_dos = DoS(test_ssh_honeypot.server_ip, test_ssh_honeypot.port, test_ssh_honeypot.username, test_ssh_honeypot.password, accepting_connections=True)

test_dos.run_dos_attack()

print()

#print("Number of threads = ", threading.active_count())

# print()
# print("Now the fuzzing attack...")
# time.sleep(3)
# test_fuzzing = Fuzzing(test_ssh_honeypot.server_ip, test_ssh_honeypot.port, test_ssh_honeypot.username, test_ssh_honeypot.password)
# test_fuzzing.fuzzing()



print("Attack(s) done")