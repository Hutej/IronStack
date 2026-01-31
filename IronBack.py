from typing import Any


class IronBack:
    def __init__(self):
        pass

    def __call__(self, environ, start_reponse) -> Any:
        print(environ)
        start_reponse("200 OK", headers=[])
        return [b"hello world"]
    
    