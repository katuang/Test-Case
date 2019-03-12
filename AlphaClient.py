#!usr/bin/python3

import time, sys, socket

curr = 0
count = 0
name = socket.gethostname()
#HOST = '192.168.100.84'
PORT = 12345

#print('Server IP Address: ',end='')
HOST = str(sys.argv[1])

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.connect((HOST, PORT))

while True:
    try:
        #client.connect((target_host, target_port))
        with open('/var/log/auth.log') as f:
            #fContent = f.readlines()
            f.seek(0,2)
            if f.tell() < curr:
                f.seek(0,0)
            else:
                f.seek(curr,0)
            for line in f:
                if ('Failed' in line) or ('Invalid' in line) or ('Accepted' in line):
                    #print(line)
                    count += 1
            curr = f.tell()
    
            client.send(('[*] ' + name + ' had '+ str(count) + ' attempts ').encode())
            
            #print(count)
        
    except IOError:
        pass
    time.sleep(2)

client.close()

