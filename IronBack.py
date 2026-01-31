from typing import Any

class IronBack:
    def __init__(self):
        self.routes = dict()

    def __call__(self, environ, start_reponse) -> Any:
        response = {}
        for path, handle_dict in self.routes.items():
            for request_method, handler in handle_dict.items():
                if environ["REQUEST_METHOD"] == request_method and path == environ["PATH_INFO"]:
                    handler(environ, response)
                    start_reponse(response["status_code"], headers = response["headers"])
                    return [(response["text"]).encode()]
                
        start_reponse("404 Not found",[])
        return [b"Not Found"]

    def get(self, path=None):
        def wrapper(handler):
            path_name = path or f"/{handler.__name__}"

            if path_name not in self.routes:
                self.routes[path_name] = {}

            self.routes[path_name]["GET"] = handler

        return wrapper