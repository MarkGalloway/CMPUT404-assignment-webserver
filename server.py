import SocketServer
import os
import email.utils

class MyWebServer(SocketServer.BaseRequestHandler):
	
	web_root = 'www'
	implemented_methods = ['GET', 'HEAD']
	
	# Potential response statuses
	status = {
		'200' : '200 OK',
		'404' : '404 Not Found',
		'501' : 'Not Implemented',
	}
	
	# Currently supported mime-types
	mimetypes = {
		'.txt' : 'text/plain',
		'.css' : 'text/css',
		'.html' : 'text/html',
	}
	
	# Status code for the response
	def getStatusCode(self, method, path):
		if method not in self.implemented_methods:
			return '501'
		
		if not os.path.isfile(path):
			return '404'
		
		return '200'
	
	# Add response fields specific to content retrieval
	def getContentFields(self, path):
		bytes = os.stat(path).st_size
		extension = os.path.splitext(path)[1]
		mimetype = self.mimetypes.get(extension, 'text/plain')
		
		return """Content-Length: {bytes}\r
Content-Type: {mimetype}\r\n""".format(**locals())

	# Read content from file and return
	def getContent(self, path):
		with open(path) as file:
			return file.read()
	
	# Gets the path from the URI in the request
	def getPath(self, uri):
		if uri[-1] == '/':
			uri += 'index.html'
		
		# norm path collapses sym links and up level references ('..' for example)
		path = os.getcwd() + "/www" + os.path.normpath(uri)
		return path
	
	# Builds the response message including headers and (if applicable) content
	def getResponse(self):
		method, uri, version = self.data.split()[:3]
		path = self.getPath(uri)
		
		print("%s" % path)

		rfc_date = email.utils.formatdate(timeval=None, localtime=False, usegmt=True)
		code = self.getStatusCode(method, path)
		status = self.status[code]
		
		if code == '200':
			content_fields = self.getContentFields(path)
			content = self.getContent(path)
		else:
			content_fields = ""
			content = ""
		
		return """HTTP/1.1 {status}\r
Date: {rfc_date}\r
{content_fields}\r
{content}""".format(**locals())
		
	def handle(self):
		self.data = self.request.recv(1024).strip()
		print ("Got a request: %s\n" % self.data.split())
		
		response = self.getResponse()
		self.request.sendall(response)

if __name__ == "__main__":
    HOST, PORT = "localhost", 8080

    SocketServer.TCPServer.allow_reuse_address = True
    # Create the server, binding to localhost on port 8080
    server = SocketServer.TCPServer((HOST, PORT), MyWebServer)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()