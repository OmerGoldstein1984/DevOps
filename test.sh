 #!bin/bash
 ssh -i "~/.ssh/key.pem" ubuntu@$1 '''/
  nmap $1
  sudo apt install net-tools
  sudo apt install net-python3
 '''
