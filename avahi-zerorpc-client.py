import csv
import time
import zerorpc
import subprocess

def get_service_ip(service_name):
    srv = None

    while True:
        avahi = subprocess.check_output(["avahi-browse","-rpt","_remote._tcp"])
        reader = csv.reader(avahi.decode().split('\n'), delimiter=';')
        for row in reader:
            if row and row[0] == "=" and service_name in row[3]:
                print("We have IP: " + row[7])
                srv = row[7] + ":" + row[8]
        if srv:
            break
        else:
            time.sleep(10)
    return srv

service_name = "sna-gw"
ip = get_service_ip(service_name)
c = zerorpc.Client()
c.connect("tcp://%s" % ip)

for request in range (10):
    print(c.hello("RPC"))
