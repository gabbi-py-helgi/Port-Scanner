import os
import platform
from datetime import datetime
raw_input = input
net = raw_input("Enter the network address: ")
net1 = net.split(".")
a = ","
net2 = net1[0]+a+net1[1]+a+net1[2]+a
st1 = int(raw_input("Enter the starting number: "))
en1 = int(raw_input("Enter the ending number: "))   
en1 = en1+1
oper = platform.system()
if (oper == "Windows"):
    ping = "ping -n 1 "
elif (oper == "Linux"):
    ping = "ping -c 1 "
else:
    ping1 = "ping -c 1 "
t1 = datetime.now()
print("Scanning In Progress")
for ip in range(st1, en1):
    addr = net2+str(ip)
    comm = ping + addr
    response = os.popen(comm)
    for line in response.readlines():
        if line.count("ttl") >= 1:
            print(addr, "is alive")
t2 = datetime.now()
total = t2-t1
print("Scanning Completed in:", total)
