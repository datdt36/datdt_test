#!/usr/bin/env python
import paramiko

k = paramiko.RSAKey.from_private_key_file("D:\Temp\id_rsa")
c = paramiko.SSHClient()

c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print ("connecting")

c.connect( hostname = "192.168.23.139", username = "datdt", pkey = k )
print ("connected")
commands = [ "ls -l /home/datdt/" ]
for command in commands:
    print ("Executing {}".format( command ))
    stdin , stdout, stderr = c.exec_command(command)
    print (stdout.read())
    print( "Errors")
    print (stderr.read())
c.close()