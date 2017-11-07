import time
import beacon
import zerorpc

while not beacon.find_all_servers(12000, b"abc"):
    print("single: %r" % beacon.find_server(12000, b"abc"))
    print("all: %r" % beacon.find_all_servers(12000, b"abc"))

print("single: %r" % beacon.find_server(12000, b"abc"))
print("all: %r" % beacon.find_all_servers(12000, b"abc"))

srv = beacon.find_server(12000, b"abc")

c = zerorpc.Client()
c.connect("tcp://%s:4242" % srv)

for request in range (10):
    print c.hello("RPC")
    time.sleep(1)
