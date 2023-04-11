import subprocess
import chardet

def ping_web(sites):
    for site in sites:
        args = ['ping', site]
        proc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
        for line in proc_ping.stdout:
            enc_site = chardet.detect(line)
            print(line.decode(enc_site['encoding']))


ping_web(['yandex.ru', 'youtube.com']) 