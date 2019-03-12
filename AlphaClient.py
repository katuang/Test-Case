#!usr/bin/python3

import time, sys, socket

current = 0
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
        with open('/var/log/auth.log') as logFile:
            #fContent = f.readlines()
            logFile.seek(0,2)
            if logFile.tell() < current:
                logFile.seek(0,0)
            else:
                logFile.seek(current,0)
            for line in logFile:
                if ('Failed' in line) or ('Invalid' in line) or ('Accepted' in line):
                    #print(line)
                    count += 1
            current = logFile.tell()
    
            client.send(('[*] ' + name + ' had '+ str(count) + ' attempts ').encode())
            
            #print(count)
        
    except IOError:
        pass
    time.sleep(2)

client.close()

