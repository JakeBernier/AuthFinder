import httplib, ssl, urllib2, socket, sys, re

if len(sys.argv) == 1:
        print "Please feed me a URL...\n\n:)\n"
        sys.exit(0)

class HTTPSConnectionV3(httplib.HTTPSConnection):
    def __init__(self, *args, **kwargs):
        httplib.HTTPSConnection.__init__(self, *args, **kwargs)
        
    def connect(self):
        sock = socket.create_connection((self.host, self.port), self.timeout)
        if self._tunnel_host:
            self.sock = sock
            self._tunnel()
        try:
            self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file, ssl_version=ssl.PROTOCOL_SSLv3)
        except ssl.SSLError, e:
            print("Trying SSLv3.")
            self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file, ssl_version=ssl.PROTOCOL_SSLv23)
            
class HTTPSHandlerV3(urllib2.HTTPSHandler):
    def https_open(self, req):
        return self.do_open(HTTPSConnectionV3, req)
# install opener
urllib2.install_opener(urllib2.build_opener(HTTPSHandlerV3()))

if __name__ == "__main__":
	for url in sys.argv[1:]:
	    	html = urllib2.urlopen(url).read()


from bs4 import BeautifulSoup, NavigableString

page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
source=soup.findAll('script',{"src":True})
for sources in source:
 print sources['src']




