# WARNING: This is a public repository!!!

This library masks namespaces for troublesome dependencies.

Currently it offers no-op alternatives for [tqdm](https://github.com/tqdm/tqdm).


# Usage

In you `setup.cfg` or `pyproject.toml` install_requires section add:

```
tqdm @ git+https://github.com/tignis/shenanigans.git@dee49cc#subdirectory=tqdm
```
