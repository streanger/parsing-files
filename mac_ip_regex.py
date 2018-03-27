import re

def mac_re(address=""):
    MAC = re.search(r'([0-9A-F]{2}[:-]){5}([0-9A-F]{2})', address, re.I).group()
    return MAC

def ip_re(address=""):
    IP = re.search(r'((2[0-5]|1[0-9]|[0-9])?[0-9]\.){3}((2[0-5]|1[0-9]|[0-9])?[0-9])', address, re.I).group()
    return IP

if __name__ == "__main__":
    s = "http://[ipaddress]/SaveData/127.0.0.1/00-0C-F1-56-98-AD/"
    print(mac_re(s))
    print(ip_re(s))
