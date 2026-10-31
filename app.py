
from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = "0.0.0.0"
PORT = 5000

class MyApp(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = """
        <html>
        <head>
            <title>Python CI CD Application</title>
        </head>
        <body>
            <h1>Welcome to My Python Web App!</h1>
            <h2>Jenkins CI Pipeline Successful</h2>
            <h2>Cloud Deployment Successful</h2>
            <p>Application deployed successfully!</p>
        </body>
        </html>
        """

        self.wfile.write(html.encode())

if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), MyApp)
    print("Server running on port 5000")
    server.serve_forever()
