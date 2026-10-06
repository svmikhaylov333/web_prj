
from http.server import BaseHTTPRequestHandler, HTTPServer


host_name = "localhost"
server_port = 8080


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        """Обрабатывает GET-запросы: возвращает страницу 'Контакты'."""

        with open('home/contacts.html', 'r', encoding='utf-8') as file:
            content = file.read()

        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode('utf-8'))

    def do_POST(self):
        """принимает POST-запрос и печатает данные в консоль"""
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')
        print(f"Получен POST-запрос:{post_data}")

        with open('home/contacts.html', 'r', encoding='utf-8') as file:
            content = file.read()
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode('utf-8'))





if __name__ == "__main__":
    web_server = HTTPServer((host_name, server_port), MyServer)  # type: ignore
    print("Server started http://%s:%s" % (host_name, server_port))

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print("Server stopped.")