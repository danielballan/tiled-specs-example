Start a server with `config.yml`.

```
tiled serve config --public config.yml
```

This config invokes a custom adapter, defined in `adapter.py` for CSV files.
It expects a certain header and informs the Tiled server that they satisfy
a certain "spec", `special_thing`.

Install the custom client-side package, `my_package`, which declares
a `tiled.special_client` entrypoint for `special_thing`.

```
pip install .
```

Connect to the server.

```
In [1]: from tiled.client import from_uri

In [2]: c = from_uri("http://localhost:8000")

In [3]: c["example"]
Out[3]: <my_package.client.CustomObject at 0x7fc325dabd60>
```

The Tiled client dispatched to the custom object via the entrypoint.

