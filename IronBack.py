from typing import Any
from response import Response

class IronBack:
    def __init__(self):
        self.routes = dict()

    def __call__(self, environ, start_reponse) -> Any:
        response = Response()
        for path, handle_dict in self.routes.items():
            for request_method, handler in handle_dict.items():
                if environ["REQUEST_METHOD"] == request_method and path == environ["PATH_INFO"]:
                    handler(environ, response)
                    response.as_wsgi(start_reponse)
                    return [(response.text).encode()]   
                
        start_reponse("404 Not found",[])
        return [b"Not Found"]

    def get(self, path=None):
        def wrapper(handler):
            path_name = path or f"/{handler.__name__}"

            if path_name not in self.routes:
                self.routes[path_name] = {}

            self.routes[path_name]["GET"] = handler

        return wrapper