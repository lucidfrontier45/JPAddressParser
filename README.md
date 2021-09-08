# JPAddressParser
Parser of Japanese Addresses

## Install

```sh
pip install jpaddressparser
```

## Usage

```python
from jpaddressparser import get_default_parser

parser = get_default_parser()
addr = parser.parse("東京都千代田区永田町１丁目７－１")
print(addr)
>>> Address(prefecture='東京都', city='千代田区', district='永田町', remained_address='1丁目7-1')
```

## Develop

This project is managed with [Poetry](https://python-poetry.org/).

```sh
poetry install
poetry run python setup.py develop
```