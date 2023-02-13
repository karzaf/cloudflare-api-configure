import os
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
token=str(input(bcolors.OKBLUE+"What is your Global API ?  "+bcolors.OKBLUE))
try:
    os.system("sudo apt upgrade -y")
    os.system("sudo apt update -y")
    os.system("sudo apt install python3-pip -y")
    os.system("sudo python3 -m pip install certbot certbot-dns-cloudflare")
    os.system("git clone https://github.com/cloudflare/python-cloudflare")
    os.system("cd python-cloudflare")
    os.system("python3 setup.py build")
    os.system("sudo python3 setup.py install")
    os.system("pip3 freeze | grep cloudflare")
    os.system(f"echo 'dns_cloudflare_api_token = ${token}' | sudo tee /root/cloudflare-api-token.ini")
    os.system(f"sudo certbot certonly --dns-cloudflare --dns-cloudflare-credentials /root/cloudflare-api-token.ini -d hcr.jpaul.io")
    print(bcolors.OKGREEN + "Cloudflare-api-configure All done!!" + bcolors.OKGREEN)
except:
   print(bcolors.WARNING + "Warning: cmd broken " + bcolors.ENDC)
   print(bcolors.WARNING + "please charge to manual it! https://github.com/karzaf/cloudflare-api-configure/blob/main/README.md" + bcolors.ENDC)
