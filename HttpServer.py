from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 设置响应状态码
        self.send_response(200)
        # 设置响应头
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        # 要返回的JSON数据
        response_data = {
            "message": "Hello, this is a JSON response from the HTTP server.",
            "status": "success"
        }
        # 将Python字典转换为JSON字符串并编码为字节
        response_json = json.dumps(response_data).encode('utf-8')
        # 发送响应体
        self.wfile.write(response_json)

def run(server_class=HTTPServer, handler_class=MyHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
