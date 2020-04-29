 #!/usr/bin/python3
import os, sys
import threading
import requests

os.system("clear")
os.system("ls")


#1
print(os.getpid())

#2
print(os.getloadavg())

#3
load_avg = os.getloadavg()
print(load_avg[1])

#4
arr = ['https://api.github.com', 'http://bilgisayar.mu.edu.tr/',
'https://www.python.org/', 'http://akrepnalan.com/ceng2034',
'https://github.com/caesarsalad/wow']

def link(string):

    x = requests.get(string)
    y=x.status_code

    if (100 <y< 300 ):

      print("The url is valid: " + string)

    else:

      print("The url is invalid " + string)

link(arr[0])

thread1 = threading.Thread(target=link, args=("https://api.github.com",))

thread2 = threading.Thread(target=link, args=("http://bilgisayar.mu.edu.tr/",))

thread3 = threading.Thread(target=link, args=('https://www.python.org/',))

thread4 = threading.Thread(target=link, args=('http://akrepnalan.com/ceng2034',))

thread5 = threading.Thread(target=link, args=('https://github.com/caesarsalad/wow',))


thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()


