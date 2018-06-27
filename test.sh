#!/bin/bash

DOMAINS=(
  'google.com'
  'g00gle.com'
  'paypal.com'
  'www.paypal.com'
  'paypal-accounts.com'
)

for i in "${DOMAINS[@]}"; do
  echo "testing: $i"
  python predict.py "$i"
done
