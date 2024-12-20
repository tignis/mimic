> [!NOTE]
> This is a public repository.

This library masks namespaces for specific dependencies.

Currently it offers no-op alternatives for:
- [tqdm](https://github.com/tqdm/tqdm)
- [certifi](https://github.com/certifi/python-certifi)

# Usage

In your `setup.cfg` or `pyproject.toml` install_requires section add:

```
tqdm @ git+https://github.com/tignis/mimic.git@d99806a#subdirectory=tqdm
certifi @ git+https://github.com/tignis/mimic.git@d99806a#subdirectory=certifi
```
