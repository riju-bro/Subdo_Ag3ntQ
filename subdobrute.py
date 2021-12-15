import requests
import socket as s
import os

G = "\033[32m"    # Green
W = "\033[0m"     # White
R = "\033[31m"    # Red
C = "\033[36m"    # Cyan
B = "\033[34m"    # Blue
Y = "\033[33m"    # Yellow
user="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
head={"User-Agent":user}
def subdomain():
  print(Y)
  os.system(f"figlet SubdoBrute")
  space=10*" "
  print(f"{C}{space}https://github.com/Ag3ntQ{W}")
  target=input(f"{B}\n[#] Enter Domain : {W}")
  print(25*"=")
  files=open("subdomains.txt")
  flag=False
  for line in files:
    line=line.strip()
    url=line+"."+target
    try:
     get_url="https://"+url
     res= requests.get(get_url,headers=head)
     if res:
      flag=True
      iip=s.gethostbyname(url)
      print(f"{G}[•] {url} [{iip}]{W}")
    except KeyboardInterrupt:
     break
     print("[ !! ] KeyboardInterrupt : Terminated")
    except Excetion as e:
    	print(25*"-")
    	print(f"{R}[•] Error Found ")
    	print(f"{e}{W}")
    	print(25*"-")
    	pass
  if flag==False:
   print(f"{R}[-] Subdomain Not Found{W}")
  else:
   pass
 
subdomain()  