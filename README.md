#python setup
```
git clone https://github.com/karzaf/cloudflare-api-configure/blob/main/cloudflare-api-easy-setup.py
python 3 cloudflare-api-easy-setup.py
```


#Manual Cloudflare-api-install

## step-1 Installing pip
```
sudo apt install python3-pip -y
```
## step-2 Installing certbot
```
sudo python3 -m pip install certbot certbot-dns-cloudflare
```
## step-3 cloudflare setup
```
git clone https://github.com/cloudflare/python-cloudflare
cd python-cloudflare
python3 setup.py build
sudo python3 setup.py install
pip3 freeze | grep cloudflare
```
## step-4 configure the api token
input the your cloudflare Global API Key
path:https://dash.cloudflare.com/profile/api-tokens
```
TOKEN="PutYourApiTokenHere"
echo "dns_cloudflare_api_token = ${TOKEN}" | sudo tee /root/cloudflare-api-token.ini
```
## step-5 Run cmd to validate the certificate.
```
sudo certbot certonly --dns-cloudflare --dns-cloudflare-credentials /root/cf-api-token.ini -d hcr.jpaul.io
```
# One click cmd
```
sudo apt install python3-pip -y
sudo python3 -m pip install certbot certbot-dns-cloudflare
git clone https://github.com/cloudflare/python-cloudflare
cd python-cloudflare
python3 setup.py build
sudo python3 setup.py install
pip3 freeze | grep cloudflare
TOKEN="PutYourApiTokenHere"
echo "dns_cloudflare_api_token = ${TOKEN}" | sudo tee /root/cloudflare-api-token.ini
sudo certbot certonly --dns-cloudflare --dns-cloudflare-credentials /root/cf-api-token.ini -d hcr.jpaul.io
```

