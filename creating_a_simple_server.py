#Creating a simple server
from http.server import BaseHTTPRequestHandler, SimpleHTTPRequestHandler, HTTPServer
my_html_file = open("2server_message.html")

#Request Handler class

class TestServer(BaseHTTPRequestHandler):
	#Get Handler
	def do_GET(self):
		#successful request handling statis code
		self.send_response(200)
		#sending Headers
		self.send_header('content-type', 'text/html')
		self.end_headers()

		#Sending back message to Client
		message = my_html_file.read()
		#Specify Encoding
		self.wfile.write(bytes(message, "utf-8"))
		my_html_file.close()
		return

def run():
	PORT = 8081
	print("Starting Server")
	#Server settings
	server_address = ('127.0.0.1', 8081)
	action = HTTPServer(server_address, TestServer)
	print('Running server now on 127.0.0.1:{}....'.format(PORT))
	action.serve_forever()

run()