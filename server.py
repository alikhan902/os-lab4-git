from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


if __name__ == "__main__":
    with ThreadingHTTPServer(("", 8080), SimpleHTTPRequestHandler) as server:
        print("Сервер запущен на порту 8080", flush=True)
        server.serve_forever()
