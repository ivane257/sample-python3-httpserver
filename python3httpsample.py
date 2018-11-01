# ORIGIN: Ivane Gegia, ivane347.com

from http.server import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 8080

# This class contains request handling methods
class MyHTTPHandler(BaseHTTPRequestHandler):
	
	# overriding GET request handler
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type","text/html")
		self.end_headers()
		
		# writing text/html content
		self.wfile.write(bytes("PLAIN TEXT: Hello World !", "utf-8"))
		self.wfile.write(bytes("<div style='color:red'>HTML: Hello div!</div>", "utf-8"))

		# accessing query string's path part and responding it
		self.wfile.write(bytes("HTTP query: "+self.path+"<br/>", "utf-8"))

		# accessing and writing HTTP header field of request
		self.wfile.write(bytes("Accept: "+self.headers["Accept"], "utf-8"))
		return

	# overriding POST request handler
	def do_POST(self):
		self.send_response(200)
		self.send_header("Content-type","text/html")
		self.end_headers()

		post_body_length = int(self.headers["content-length"])
		post_concent = self.rfile.read(post_body_length)
		self.wfile.write(bytes("<div>"+post_concent+"</div>", "utf-8"))
		return

if __name__ == "__main__":
	try:
		# Create HTTPServer and pass in our HTTP requests handler
		server = HTTPServer(("", PORT_NUMBER), MyHTTPHandler)
		print("HTTP server started on port: ", PORT_NUMBER)
		
		# server starts and listens forever
		server.serve_forever()
	
	except KeyboardInterrupt:
		print("CTRL+C received, shutting down the web server")
		server.socket.close()

