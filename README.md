> [!NOTE]
> This is a public repository.

This library masks namespaces for specific dependencies.

Currently it offers no-op alternatives for [tqdm](https://github.com/tqdm/tqdm).

# Usage

In your `setup.cfg` or `pyproject.toml` install_requires section add:

```
tqdm @ git+https://github.com/tignis/mimic.git@9f9e8e9#subdirectory=tqdm
```
