from http.server import BaseHTTPRequestHandler, HTTPServer

# This is a simple HTTP request handler
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Set the response status code (200 OK)
        self.send_response(200)
        # Set the Content-Type header
        self.send_header('Content-type', 'text/html')
        # End the headers section
        self.end_headers()
        # Write the response body
        self.wfile.write(b"Hello from Python Docker!")
        debug = True  # Unused variable (SonarQube code smell)

# Function to run the server
def run(server_class=HTTPServer, handler_class=MyHandler, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd on port ' + str(port) + '...')  # Prefer f-strings (readability/code smell)
    httpd.serve_forever()

# This block ensures the server starts when the script is executed
if __name__ == '__main__':
    run()
