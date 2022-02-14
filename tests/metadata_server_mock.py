import json
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

_MDS_ADDRESS = ("localhost", 50052)


def metadata_server(token):
    class MetadataHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            data = _MDS_TOKEN = json.dumps({
                "access_token": token,
                "expires_in": 100,
                "token_type": "Bearer"
            }).encode("utf-8")

            self.send_response(200)
            self.send_header('Content-Length', len(data))
            self.end_headers()
            self.wfile.write(data)

    srv = HTTPServer(_MDS_ADDRESS, MetadataHandler)
    thread = threading.Thread(target=srv.serve_forever)
    thread.daemon = True
    thread.start()

    srv.addr = "{}:{}".format(_MDS_ADDRESS[0], _MDS_ADDRESS[1])

    return srv
