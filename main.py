import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

# Criar um arquivo para armazenar as notas
notas_file = "notas.json"

# Classe que trata as requisições HTTP
class MyHandler(BaseHTTPRequestHandler):
    def _send_response(self, status_code, message):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(message).encode('utf-8'))

    def do_GET(self):
        if self.path == '/Mostrar':
            try:
                with open(notas_file, 'r') as f:
                    notas = json.load(f)
                self._send_response(200, notas)
            except FileNotFoundError:
                self._send_response(200, [])
        else:
            self._send_response(404, {"error": "Endpoint não encontrado"})

    def do_POST(self):
        if self.path == '/adicionar':
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            data = json.loads(body.decode('utf-8'))
            try:
                with open(notas_file, 'r') as f:
                    notas = json.load(f)
            except FileNotFoundError:
                notas = []
            
            notas.append(data)

            with open(notas_file, 'w') as f:
                json.dump(notas, f)

            self._send_response(200, {"message": "Nota adicionada com sucesso"})
        else:
            self._send_response(404, {"error": "Endpoint não encontrado"})

    def do_DELETE(self):
        if self.path.startswith('/delete'):
            parsed_url = urlparse(self.path)
            query_params = parse_qs(parsed_url.query)
            if 'titulo' in query_params:
                titulo = query_params['titulo'][0]
                try:
                    with open(notas_file, 'r') as f:
                        notas = json.load(f)
                    notas = [nota for nota in notas if nota['titulo'] != titulo]
                    with open(notas_file, 'w') as f:
                        json.dump(notas, f)
                    self._send_response(200, {"message": f"Nota com título '{titulo}' excluída com sucesso"})
                except FileNotFoundError:
                    self._send_response(404, {"error": "Arquivo de notas não encontrado"})
            else:
                self._send_response(400, {"error": "Parâmetro 'titulo' ausente na requisição"})
        else:
            self._send_response(404, {"error": "Endpoint não encontrado"})

def run(server_class=HTTPServer, handler_class=MyHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Servidor rodando na porta {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
