# Arrow Flight RPC Python Example

## Dependency
https://github.com/apache/arrow/tree/main/python/examples/flight

## MacOS Environment
```bash
brew install virtualenv openssl
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Flight Server
```bash
# By default, it listens on localhost:5005
.venv/bin/python server/server.py
```

## Flight Client
```bash
# Generate a data sample csv file
.venv/bin/python client/generate-csv.py client/samples.csv

# Read local csv file, transform csv to arrow and send it to flight server
.venv/bin/python client/client.py put 127.0.0.1:5005 client/samples.csv

# List all available flights of flight server
.venv/bin/python client/client.py list 127.0.0.1:5005

# Load remote flight and print it out in the local environment
.venv/bin/python client/client.py get -p client/samples.csv 127.0.0.1:5005
```

## Communication Encryption by mTLS
```bash
# Generate Certificate Chain
cd mtls
bash create_certificates.sh

# Run Server
.venv/bin/python server/server.py \
    --tls ./mtls/output/server.crt ./mtls/output/server.key

# Run Client
.venv/bin/python client/client.py put 127.0.0.1:5005 client/samples.csv \
    --tls --tls-roots ./mtls/output/ca.crt --mtls ./mtls/output/client.crt ./mtls/output/client.key
```