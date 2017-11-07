import beacon
import zerorpc

b = beacon.Beacon(12000, "abc")
b.daemon = True
b.start()

class HelloRPC(object):
    def hello(self, name):
        return "Hello, %s" % name

s = zerorpc.Server(HelloRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()
