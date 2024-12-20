from sys import version_info
import certifi

if version_info < (3, 9):
    from importlib.resources import path

    def where():
        with path(certifi, "root_store.certs") as p:
            return str(p)
else:
    from importlib.resources import files

    def where():
        return str(files(certifi)/"root_store.certs")
