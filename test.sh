#!/bin/bash

DOMAINS="google.com,g00gle.com,paypal.com,secure-paypal.com,securitymywindowspcsystem.info,bank.wellsbankingsecurelogin.com,apple-gps-tracker.xyz"

python predict.py "${DOMAINS}"
