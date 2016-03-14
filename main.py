import mechanize
from threading import *

sm = Semaphore(1)


br = mechanize.Browser()

def worker_thread():
    with open('sqltext.txt','r') as tx:
        for line in tx:
            try:
                data = br.open(line.strip('\n') + "'").read()
            except:
                continue
            if 'corresponds to your MySQL' in data:
                sm.acquire()
                print '[+] ' + line.strip('\n')  + "'<---- Found"
                f = open('result.txt','a')
                f.write(line)
                f.close()
                sm.release()

def main():
    for _ in range(10):
        t = Thread(target=worker_thread())
        t.setDaemon(True)
        t.start()


if __name__ == '__main__':
    main()