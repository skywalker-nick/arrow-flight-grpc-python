# Python Arrow Flight RPC Example

## Dependency
https://github.com/apache/arrow/tree/main/python/examples/flight

## MacOS Environment
```bash
brew install virtualenv
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Flight Server
```bash
# By default, it listens on localhost:5005
python server/server.py
```

## Flight Client
```bash
# Generate a data sample csv file
python client/generate-csv.py

# Read local csv file, transform csv to arrow and send it to flight server
python client/client.py put 127.0.0.1:5005 client/samples.csv

# List all available flights of flight server
python client/client.py list 127.0.0.1:5005

# Load remote flight and print it out in the local environment
python client/client.py get -p client/samples.csv 127.0.0.1:5005
```