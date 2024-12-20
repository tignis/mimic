from importlib.resources import files
import certifi

def where():
    return str(files(certifi)/"root_store.certs")
