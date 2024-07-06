#!/bin/bash

set -e

PLAIN_DIR="./output"
CONFIG_DIR="./"
VALIDATION_DAYS=36500

mkdir -p $PLAIN_DIR

# generate plain text certificates
openssl genrsa -out "${PLAIN_DIR}"/ca.key 2048
openssl req -new -x509 -key "${PLAIN_DIR}"/ca.key -config "$CONFIG_DIR"/ca.cnf -days "${VALIDATION_DAYS}" -out "${PLAIN_DIR}"/ca.crt

openssl genrsa -out "${PLAIN_DIR}"/server.key 2048
openssl genrsa -out "${PLAIN_DIR}"/client.key 2048

openssl req -new -sha256 -key "${PLAIN_DIR}"/server.key -config "$CONFIG_DIR"/server.cnf -out "${PLAIN_DIR}"/server.csr
openssl req -new -sha256 -key "${PLAIN_DIR}"/client.key -config "$CONFIG_DIR"/client.cnf -out "${PLAIN_DIR}"/client.csr

openssl x509 -req -in "${PLAIN_DIR}"/server.csr -CA "${PLAIN_DIR}"/ca.crt -CAkey "${PLAIN_DIR}"/ca.key -CAcreateserial \
      -sha256 -days "${VALIDATION_DAYS}" -out "${PLAIN_DIR}"/server.crt -extfile "$CONFIG_DIR"/server.cnf -extensions req_ext
openssl x509 -req -in "${PLAIN_DIR}"/client.csr -CA "${PLAIN_DIR}"/ca.crt -CAkey "${PLAIN_DIR}"/ca.key -CAcreateserial \
      -sha256 -days "${VALIDATION_DAYS}" -out "${PLAIN_DIR}"/client.crt -extfile "$CONFIG_DIR"/client.cnf -extensions req_ext

echo "All done. Certificates should be found under '${PLAIN_DIR}'"