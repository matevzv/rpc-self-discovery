import csv
import time
import zerorpc
import subprocess

srv = None

while True:
    avahi = subprocess.check_output(["avahi-browse", "-rpt", "_remote._tcp"])
    reader = csv.reader(avahi.split('\n'), delimiter=';')
    for row in reader:
        if row and row[0] == "=" and "sna-lgtc" in row[6]:
            print "We have IP: " + row[7]
            srv = row[7] + ":" + row[8]
    if srv:
        break
    else:
        time.sleep(10)

c = zerorpc.Client()
c.connect("tcp://%s" % srv)

for request in range (10):
    print c.hello("RPC")
    time.sleep(1)
